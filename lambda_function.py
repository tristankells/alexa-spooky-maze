# -*- coding: utf-8 -*-

# This is a High Low Guess game Alexa Skill.
# The skill serves as a simple sample on how to use the
# persistence attributes and persistence adapter features in the SDK.
import random
import logging

from ask_sdk.standard import StandardSkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_model.ui import SimpleCard

from ask_sdk_model import Response

SKILL_NAME = 'High Low Game'
sb = StandardSkillBuilder(table_name="High-Low-Game", auto_create_table=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    """Handler for Skill Launch.

    Get the persistence attributes, to figure out the game state.
    """
    # type: (HandlerInput) -> Response
    attr = handler_input.attributes_manager.persistent_attributes
    if not attr:
        attr['ended_session_count'] = 0
        attr['games_played'] = 0
        attr['game_state'] = 'ENDED'
        attr['player_position_x'] = 0
        attr['player_position_y'] = 0
        attr['number_turns_remaining'] = 8

    handler_input.attributes_manager.session_attributes = attr

    speech_text = (
        "Welcome to the crazy maze (insert audio here) "
        "<audio src='soundbank://soundlibrary/animals/amzn_sfx_bear_groan_roar_01'/>")
    reprompt = "Say yes to start the game or no to quit."

    handler_input.response_builder.speak(speech_text).ask(reprompt)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
    """Handler for Help Intent."""
    # type: (HandlerInput) -> Response
    speech_text = (
        "I am thinking of a number between zero and one hundred, try to "
        "guess it and I will tell you if you got it or it is higher or "
        "lower")
    reprompt = "Try saying a number."

    handler_input.response_builder.speak(speech_text).ask(reprompt)
    return handler_input.response_builder.response


@sb.request_handler(
    can_handle_func=lambda input:
        is_intent_name("AMAZON.CancelIntent")(input) or
        is_intent_name("AMAZON.StopIntent")(input))
def cancel_and_stop_intent_handler(handler_input):
    """Single handler for Cancel and Stop Intent."""
    # type: (HandlerInput) -> Response
    speech_text = "Thanks for playing!!"

    handler_input.response_builder.speak(
        speech_text).set_should_end_session(True)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_request_type("SessionEndedRequest"))
def session_ended_request_handler(handler_input):
    """Handler for Session End."""
    # type: (HandlerInput) -> Response
    logger.info(
        "Session ended with reason: {}".format(
            handler_input.request_envelope.request.reason))
    return handler_input.response_builder.response


def currently_playing(handler_input):
    """Function that acts as can handle for game state."""
    # type: (HandlerInput) -> bool
    is_currently_playing = False
    session_attr = handler_input.attributes_manager.session_attributes

    if ("game_state" in session_attr
            and session_attr['game_state'] == "STARTED"):
        is_currently_playing = True

    return is_currently_playing


@sb.request_handler(can_handle_func=lambda input:
                    not currently_playing(input) and
                    is_intent_name("AMAZON.YesIntent")(input))
def yes_handler(handler_input):
    """Handler for Yes Intent, only if the player said yes for
    a new game.
    """
    # type: (HandlerInput) -> Response
    session_attr = handler_input.attributes_manager.session_attributes
    session_attr['game_state'] = "STARTED"
    session_attr['guess_number'] = random.randint(0, 100)
    session_attr['no_of_guesses'] = 0

    speech_text = "Great! Try saying a number to start the game."
    reprompt = "Try saying a number."

    handler_input.response_builder.speak(speech_text).ask(reprompt)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=lambda input:
                    not currently_playing(input) and
                    is_intent_name("AMAZON.NoIntent")(input))
def no_handler(handler_input):
    """Handler for No Intent, only if the player said no for
    a new game.
    """
    # type: (HandlerInput) -> Response
    session_attr = handler_input.attributes_manager.session_attributes
    session_attr['game_state'] = "ENDED"
    session_attr['ended_session_count'] += 1

    handler_input.attributes_manager.persistent_attributes = session_attr
    handler_input.attributes_manager.save_persistent_attributes()

    speech_text = "Ok. See you next time!!"

    handler_input.response_builder.speak(speech_text)
    return handler_input.response_builder.response



# class MoveIntentHandler(AbstractRequestHandler):
#     """Handler for Movement Intent."""
#     def can_handle(self, handler_input):
#         # type: (HandlerInput) -> bool
#         return is_intent_name("MoveIntent")(handler_input)

#     def handle(self, handler_input):
#         # type: (HandlerInput) -> Response
#         turns = 5
#         speech_text = "You tried to move :D. Your turn is " + str(turns)
#         handler_input.response_builder.speak(speech_text).set_card(
#             SimpleCard("Hello World", speech_text)).set_should_end_session(
#             True)
#         return handler_input.response_builder.response

# Handle the Movement invocation (forward, back, down, up)
@sb.request_handler(can_handle_func=lambda input:
                    is_intent_name("MoveIntent")(input))
def movement_handler(handler_input):
    """Handler for processing guess with target."""
    # type: (HandlerInput) -> Response
    session_attr = handler_input.attributes_manager.session_attributes # session variables

    direction = str(handler_input.request_envelope.request.intent.slots["movement"].value) # value of movement slot
    movePostion(direction, session_attr) # adjust x or y co-ordinates

    session_attr["number_turns_remaining"] -= 1 #decrease turns remaining 
    turns_remaining = session_attr["number_turns_remaining"] #value of turns remaining

    speech_text = "You tried to move " + direction + ". You are at position x = " + str(session_attr['player_position_x']) + " and y = " + str(session_attr['player_position_y'])  + ". Your have " + str(turns_remaining) + " turns remaining"
    reprompt = "Where now?"
    handler_input.response_builder.speak(speech_text).ask(reprompt)
    return handler_input.response_builder.response


def moveForward(session_attr):
    session_attr['player_position_x'] +=1

def moveLeft(session_attr):
    session_attr['player_position_y'] +=1

def moveBack(session_attr):
   session_attr['player_position_x'] -=1

def moveRight(session_attr):
    session_attr['player_position_y'] -=1

def movePostion(direction, handler_input):
    switcher = {
        "forward": moveForward,
        "left": moveLeft,
        "back": moveBack,
        "right": moveRight
    }
    # Get the function from switcher dictionary
    func = switcher.get(direction, lambda: "nothing")
    # Execute the function
    return func(handler_input)


@sb.request_handler(can_handle_func=lambda input:
                    currently_playing(input) and
                    is_intent_name("NumberGuessIntent")(input))
def number_guess_handler(handler_input):
    """Handler for processing guess with target."""
    # type: (HandlerInput) -> Response
    session_attr = handler_input.attributes_manager.session_attributes
    target_num = session_attr["guess_number"]
    guess_num = int(handler_input.request_envelope.request.intent.slots[
        "number"].value)

    session_attr["no_of_guesses"] += 1

    if guess_num > target_num:
        speech_text = (
            "{} is too high. Try saying a smaller number.".format(guess_num))
        reprompt = "Try saying a smaller number."
    elif guess_num < target_num:
        speech_text = (
            "{} is too low. Try saying a larger number.".format(guess_num))
        reprompt = "Try saying a larger number."
    elif guess_num == target_num:
        speech_text = (
            "Congratulations. {} is the correct guess. "
            "You guessed the number in {} guesses. "
            "Would you like to play a new game?".format(
                guess_num, session_attr["no_of_guesses"]))
        reprompt = "Say yes to start a new game or no to end the game"
        session_attr["games_played"] += 1
        session_attr["game_state"] = "ENDED"

        handler_input.attributes_manager.persistent_attributes = session_attr
        handler_input.attributes_manager.save_persistent_attributes()
    else:
        speech_text = "Sorry, I didn't get that. Try saying a number."
        reprompt = "Try saying a number."

    handler_input.response_builder.speak(speech_text).ask(reprompt)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=lambda input:
                    is_intent_name("AMAZON.FallbackIntent")(input) or
                    is_intent_name("AMAZON.YesIntent")(input) or
                    is_intent_name("AMAZON.NoIntent")(input))
def fallback_handler(handler_input):
    """AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale,
    so it is safe to deploy on any locale.
    """
    # type: (HandlerInput) -> Response
    session_attr = handler_input.attributes_manager.session_attributes

    if ("game_state" in session_attr and
            session_attr["game_state"]=="STARTED"):
        speech_text = (
            "The {} skill can't help you with that.  "
            "Try guessing a number between 0 and 100. ".format(SKILL_NAME))
        reprompt = "Please guess a number between 0 and 100."
    else:
        speech_text = (
            "The {} skill can't help you with that.  "
            "It will come up with a number between 0 and 100 and "
            "you try to guess it by saying a number in that range. "
            "Would you like to play?".format(SKILL_NAME))
        reprompt = "Say yes to start the game or no to quit."

    handler_input.response_builder.speak(speech_text).ask(reprompt)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=lambda input: True)
def unhandled_intent_handler(handler_input):
    """Handler for all other unhandled requests."""
    # type: (HandlerInput) -> Response
    speech = "Say yes to continue or no to end the game!!"
    handler_input.response_builder.speak(speech).ask(speech)
    return handler_input.response_builder.response


@sb.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(handler_input, exception):
    """Catch all exception handler, log exception and
    respond with custom message.
    """
    # type: (HandlerInput, Exception) -> Response
    logger.error(exception, exc_info=True)
    speech = "Sorry, I can't understand that. Please say again!!"
    handler_input.response_builder.speak(speech).ask(speech)
    return handler_input.response_builder.response


@sb.global_response_interceptor()
def log_response(handler_input, response):
    """Response logger."""
    # type: (HandlerInput, Response) -> None
    logger.info("Response: {}".format(response))

# sb.add_request_handler(MoveIntentHandler())

lambda_handler = sb.lambda_handler()
