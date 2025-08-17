# 17735769 - Hound Nose

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Bastok Mines (ID: 234) |
| Block Size       | 372 bytes              |
| Total Events     | 2                      |
| References Count | 28                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [132](#event-132)     | 0x0001       |    235 |             69 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2AC9      |       10953 |
|       1 | 0x2ACA      |       10954 |
|       2 | 0x0000      |           0 |
|       3 | 0x2ACB      |       10955 |
|       4 | 0x2ACD      |       10957 |
|       5 | 0x0001      |           1 |
|       6 | 0x2ACE      |       10958 |
|       7 | 0x2ACF      |       10959 |
|       8 | 0x2AD0      |       10960 |
|       9 | 0x0002      |           2 |
|      10 | 0x2AD1      |       10961 |
|      11 | 0x2AD2      |       10962 |
|      12 | 0x0003      |           3 |
|      13 | 0x2AD3      |       10963 |
|      14 | 0x2AD4      |       10964 |
|      15 | 0x0004      |           4 |
|      16 | 0x2AD5      |       10965 |
|      17 | 0x2AD6      |       10966 |
|      18 | 0x0005      |           5 |
|      19 | 0x2AD7      |       10967 |
|      20 | 0x0006      |           6 |
|      21 | 0x2AD8      |       10968 |
|      22 | 0x2AD9      |       10969 |
|      23 | 0x2ADA      |       10970 |
|      24 | 0x2ADB      |       10971 |
|      25 | 0x0007      |           7 |
|      26 | 0x2ADD      |       10973 |
|      27 | 0x2ADC      |       10972 |

## String References

- **10953**: Welcome to the auction house. Do you have any questions about our establishment?
- **10954**: What do you want to know? [What is the auction house?/How are auctions run?/Are there any fees?/Are there any limits?/How do you check up on merchandise?/How do you remove an item?/My "Sales Status" list is full!/Nothing right now.]
- **10955**: Auction houses can be found in all of Vana'diel's major cities. Here adventurers gather to bid on battle spoils, unwanted items, old armor...almost anything.
- **10957**: Adventurers may use any auction house regardless of nationality.
- **10958**: The first adventurer to bid at or above the asking price will automatically purchase the product.
- **10959**: Once put up for auction, merchandise will remain there for a maximum of thirty weeks Vana'diel time (nine-and-a-half days Earth time).
- **10960**: If merchandise does not sell within this time limit, it will be returned to the seller's current residence.
- **10961**: Transaction fees are proportional to the amount for which an item is put up on auction. The method of calculating this fee is different for single items and stackable items.
- **10962**: A transaction fee is collected when any merchandise is put up for auction. This fee is nonrefundable.
- **10963**: The International Auction House Committee, or IAHC, has declared that a maximum of seven items may be put up for auction at one time.
- **10964**: However, the IAHC has recently removed the limit to how many items one may purchase.
- **10965**: A small amount of time is required before new merchandise appears on our bid list.
- **10966**: Once an item appears on your "Sales Status" list, it may not immediately appear on the bid list. If you do not see your item on the bid list, try looking again at a later time.
- **10967**: If you would like to withdraw an item from an auction, you must travel to the auction house, and select "Stop Sale" from the "Sales Status" menu.
- **10968**: To remove an item from your "Sales Status" list, you must visit an auction counter to acknowledge the sale or return of your merchandise.
- **10969**: Otherwise, previously sold or returned items will fill up your list and prevent you from selling any more merchandise.
- **10970**: At any auction counter, open the "Sales Status" menu and acknowledge the transaction to clear it from the list.
- **10971**: Press the confirm button to remove any transaction colored yellow (sold) or red (returned).
- **10972**: Is there anything else you would like to know?
- **10973**: In the past, many have amassed great wealth through the auction house. I hope you find fortune, too!

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 132

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 235 bytes |
| Instructions | 66        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    06 00 00 1E F0 FF FF  7F 1D 00 80 23 24 01 80   ...........#$..
0010: 02 80 00 00 25 02 00 10  02 80 00 2F 00 1D 03 80  ....%....../....
0020: 23 1D 04 80 23 3C 00 00  02 80 05 80 01 E3 00 02  #...#<..........
0030: 00 10 05 80 00 4D 00 1D  06 80 23 1D 07 80 23 1D  .....M....#...#.
0040: 08 80 23 3C 00 00 05 80  05 80 01 E3 00 02 00 10  ..#<............
0050: 09 80 00 67 00 1D 0A 80  23 1D 0B 80 23 3C 00 00  ...g....#...#<..
0060: 09 80 05 80 01 E3 00 02  00 10 0C 80 00 81 00 1D  ................
0070: 0D 80 23 1D 0E 80 23 3C  00 00 0C 80 05 80 01 E3  ..#...#<........
0080: 00 02 00 10 0F 80 00 9B  00 1D 10 80 23 1D 11 80  ............#...
0090: 23 3C 00 00 0F 80 05 80  01 E3 00 02 00 10 12 80  #<..............
00A0: 00 B1 00 1D 13 80 23 3C  00 00 12 80 05 80 01 E3  ......#<........
00B0: 00 02 00 10 14 80 00 D3  00 1D 15 80 23 1D 16 80  ............#...
00C0: 23 1D 17 80 23 1D 18 80  23 3C 00 00 14 80 05 80  #...#...#<......
00D0: 01 E3 00 02 00 10 19 80  00 E3 00 1D 1A 80 23 21  ..............#!
00E0: 01 E3 00 1D 1B 80 23 01  0D 00 21 00              ......#...!.    
```

#### Opcodes

```
  0: 0x0001 [0x06] ExtData[1]->WorkLocal[0] = 0
  1: 0x0004 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=10953*)
    → "Welcome to the auction house. Do you have any questions about our establishment?"
  3: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000D [0x24] CREATE_DIALOG(message_id=10954*, default_option=0*, option_flags=ExtData[1]->WorkLocal[0])
    → "What do you want to know? [What is the auction house?/How are auctions run?/Are there any fees?/Are there any limits?/How do you check up on merchandise?/How do you remove an item?/My "Sales Status" list is full!/Nothing right now.]"
  5: 0x0014 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0015 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x002F
  7: 0x001D [0x1D] PRINT_EVENT_MESSAGE(message_id=10955*)
    → "Auction houses can be found in all of Vana'diel's major cities. Here adventurers gather to bid on battle spoils, unwanted items, old armor...almost anything."
  8: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0021 [0x1D] PRINT_EVENT_MESSAGE(message_id=10957*)
    → "Adventurers may use any auction house regardless of nationality."
 10: 0x0024 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0025 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=0*, condition_work_offset=1*)
 12: 0x002C [0x01] GOTO 0x00E3
 13: 0x002F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x004D
 14: 0x0037 [0x1D] PRINT_EVENT_MESSAGE(message_id=10958*)
    → "The first adventurer to bid at or above the asking price will automatically purchase the product."
 15: 0x003A [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x003B [0x1D] PRINT_EVENT_MESSAGE(message_id=10959*)
    → "Once put up for auction, merchandise will remain there for a maximum of thirty weeks Vana'diel time (nine-and-a-half days Earth time)."
 17: 0x003E [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x003F [0x1D] PRINT_EVENT_MESSAGE(message_id=10960*)
    → "If merchandise does not sell within this time limit, it will be returned to the seller's current residence."
 19: 0x0042 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0043 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=1*, condition_work_offset=1*)
 21: 0x004A [0x01] GOTO 0x00E3
 22: 0x004D [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0067
 23: 0x0055 [0x1D] PRINT_EVENT_MESSAGE(message_id=10961*)
    → "Transaction fees are proportional to the amount for which an item is put up on auction. The method of calculating this fee is different for single items and stackable items."
 24: 0x0058 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x0059 [0x1D] PRINT_EVENT_MESSAGE(message_id=10962*)
    → "A transaction fee is collected when any merchandise is put up for auction. This fee is nonrefundable."
 26: 0x005C [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x005D [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=2*, condition_work_offset=1*)
 28: 0x0064 [0x01] GOTO 0x00E3
 29: 0x0067 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0081
 30: 0x006F [0x1D] PRINT_EVENT_MESSAGE(message_id=10963*)
    → "The International Auction House Committee, or IAHC, has declared that a maximum of seven items may be put up for auction at one time."
 31: 0x0072 [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x0073 [0x1D] PRINT_EVENT_MESSAGE(message_id=10964*)
    → "However, the IAHC has recently removed the limit to how many items one may purchase."
 33: 0x0076 [0x23] WAIT_FOR_DIALOG_INTERACTION
 34: 0x0077 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=3*, condition_work_offset=1*)
 35: 0x007E [0x01] GOTO 0x00E3
 36: 0x0081 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x009B
 37: 0x0089 [0x1D] PRINT_EVENT_MESSAGE(message_id=10965*)
    → "A small amount of time is required before new merchandise appears on our bid list."
 38: 0x008C [0x23] WAIT_FOR_DIALOG_INTERACTION
 39: 0x008D [0x1D] PRINT_EVENT_MESSAGE(message_id=10966*)
    → "Once an item appears on your "Sales Status" list, it may not immediately appear on the bid list. If you do not see your item on the bid list, try looking again at a later time."
 40: 0x0090 [0x23] WAIT_FOR_DIALOG_INTERACTION
 41: 0x0091 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=4*, condition_work_offset=1*)
 42: 0x0098 [0x01] GOTO 0x00E3
 43: 0x009B [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x00B1
 44: 0x00A3 [0x1D] PRINT_EVENT_MESSAGE(message_id=10967*)
    → "If you would like to withdraw an item from an auction, you must travel to the auction house, and select "Stop Sale" from the "Sales Status" menu."
 45: 0x00A6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 46: 0x00A7 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=5*, condition_work_offset=1*)
 47: 0x00AE [0x01] GOTO 0x00E3
 48: 0x00B1 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x00D3
 49: 0x00B9 [0x1D] PRINT_EVENT_MESSAGE(message_id=10968*)
    → "To remove an item from your "Sales Status" list, you must visit an auction counter to acknowledge the sale or return of your merchandise."
 50: 0x00BC [0x23] WAIT_FOR_DIALOG_INTERACTION
 51: 0x00BD [0x1D] PRINT_EVENT_MESSAGE(message_id=10969*)
    → "Otherwise, previously sold or returned items will fill up your list and prevent you from selling any more merchandise."
 52: 0x00C0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 53: 0x00C1 [0x1D] PRINT_EVENT_MESSAGE(message_id=10970*)
    → "At any auction counter, open the "Sales Status" menu and acknowledge the transaction to clear it from the list."
 54: 0x00C4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 55: 0x00C5 [0x1D] PRINT_EVENT_MESSAGE(message_id=10971*)
    → "Press the confirm button to remove any transaction colored yellow (sold) or red (returned)."
 56: 0x00C8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 57: 0x00C9 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=6*, condition_work_offset=1*)
 58: 0x00D0 [0x01] GOTO 0x00E3
 59: 0x00D3 [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x00E3
 60: 0x00DB [0x1D] PRINT_EVENT_MESSAGE(message_id=10973*)
    → "In the past, many have amassed great wealth through the auction house. I hope you find fortune, too!"
 61: 0x00DE [0x23] WAIT_FOR_DIALOG_INTERACTION
 62: 0x00DF [0x21] END_EVENT

SUBROUTINE_00E3:
 63: 0x00E3 [0x1D] PRINT_EVENT_MESSAGE(message_id=10972*)
    → "Is there anything else you would like to know?"
 64: 0x00E6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 65: 0x00E7 [0x01] GOTO 0x000D
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00E0 [0x01] GOTO 0x00E3
# Dead code (unreachable instructions):
     0x00EA [0x21] END_EVENT
     0x00EB [0x00] END_REQSTACK()
```
