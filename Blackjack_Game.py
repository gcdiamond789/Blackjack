from blackjack_helper import *

# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
hand_value = draw_starting_hand("YOUR")
user_hand = hand_value
card_value = 0
while hand_value < 21:
    # should_hit = ''
    # while should_hit != 'y' and should_hit != 'n':
    #      should_hit = input('You have ' + str(hand_value) + '. Hit (y/n)? ')
    #      if should_hit != 'y' and should_hit != 'n':
    #          print("Sorry I didn't get that.")
    # if should_hit == 'n':
    #     break
    # card_value = draw_card()
    # hand_value = hand_value + card_value
        
    should_hit = input('You have ' + str(hand_value) + ". Hit (y/n)? ")
    if should_hit == 'n':
        break
    elif should_hit == 'y':
        card_value = draw_card()
    else:
        print("Sorry I didn't get that.")
    hand_value = hand_value + card_value
user_hand = hand_value
print_end_turn_status(user_hand)

#code for dealer
dealer_hand_value = draw_starting_hand("DEALER")
dealer_hand = dealer_hand_value
while dealer_hand_value < 17:
    print("Dealer has " + str(dealer_hand_value) + ".")
    card_value = draw_card()
    dealer_hand_value = dealer_hand_value + card_value
    dealer_hand = dealer_hand_value
print_end_turn_status(dealer_hand)
#final RESULT
print_end_game_status(user_hand, dealer_hand)
