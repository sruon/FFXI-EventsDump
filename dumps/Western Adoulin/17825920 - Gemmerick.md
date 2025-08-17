# 17825920 - Gemmerick

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Western Adoulin (ID: 256) |
| Block Size       | 380 bytes                 |
| Total Events     | 3                         |
| References Count | 28                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [2](#event-2)         | 0x0001       |      1 |              1 |
| [5](#event-5)         | 0x0002       |    235 |             69 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C00      |        7168 |
|       1 | 0x1C01      |        7169 |
|       2 | 0x0000      |           0 |
|       3 | 0x1C02      |        7170 |
|       4 | 0x1C04      |        7172 |
|       5 | 0x0001      |           1 |
|       6 | 0x1C05      |        7173 |
|       7 | 0x1C06      |        7174 |
|       8 | 0x1C07      |        7175 |
|       9 | 0x0002      |           2 |
|      10 | 0x1C08      |        7176 |
|      11 | 0x1C09      |        7177 |
|      12 | 0x0003      |           3 |
|      13 | 0x1C0A      |        7178 |
|      14 | 0x1C0B      |        7179 |
|      15 | 0x0004      |           4 |
|      16 | 0x1C0C      |        7180 |
|      17 | 0x1C0D      |        7181 |
|      18 | 0x0005      |           5 |
|      19 | 0x1C0E      |        7182 |
|      20 | 0x0006      |           6 |
|      21 | 0x1C0F      |        7183 |
|      22 | 0x1C10      |        7184 |
|      23 | 0x1C11      |        7185 |
|      24 | 0x1C12      |        7186 |
|      25 | 0x0007      |           7 |
|      26 | 0x1C14      |        7188 |
|      27 | 0x1C13      |        7187 |

## String References

- **7168**: Welcome to the auction house. Do you have any questions about our establishment?
- **7169**: What do you want to know? [What is the auction house?/How are auctions run?/Are there any fees?/Are there any limits?/How do you check up on merchandise?/How do you remove an item?/My "Sales Status" list is full!/Nothing right now.]
- **7170**: Auction houses can be found in all of Vana'diel's major cities. Here adventurers gather to bid on battle spoils, unwanted items, old armor...almost anything.
- **7172**: Adventurers may use any auction house regardless of nationality.
- **7173**: The first adventurer to bid at or above the asking price will automatically purchase the product.
- **7174**: Once put up for auction, merchandise will remain there for a maximum of thirty weeks Vana'diel time (nine-and-a-half days Earth time).
- **7175**: If merchandise does not sell within this time limit, it will be returned to the seller's current residence.
- **7176**: Transaction fees are proportional to the amount for which an item is put up on auction. The method of calculating this fee is different for single items and stackable items.
- **7177**: A transaction fee is collected when any merchandise is put up for auction. This fee is nonrefundable.
- **7178**: The International Auction House Committee, or IAHC, has declared that a maximum of seven items may be put up for auction at one time.
- **7179**: However, the IAHC has recently removed the limit to how many items one may purchase.
- **7180**: A small amount of time is required before new merchandise appears on our bid list.
- **7181**: Once an item appears on your "Sales Status" list, it may not immediately appear on the bid list. If you do not see your item on the bid list, try looking again at a later time.
- **7182**: If you would like to withdraw an item from an auction, you must travel to the auction house, and select "Stop Sale" from the "Sales Status" menu.
- **7183**: To remove an item from your "Sales Status" list, you must visit an auction counter to acknowledge the sale or return of your merchandise.
- **7184**: Otherwise, previously sold or returned items will fill up your list and prevent you from selling any more merchandise.
- **7185**: At any auction counter, open the "Sales Status" menu and acknowledge the transaction to clear it from the list.
- **7186**: Press the confirm button to remove any transaction colored yellow (sold) or red (returned).
- **7187**: Is there anything else you would like to know?
- **7188**: In the past, many have amassed great wealth through the auction house. I hope you find fortune, too!

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

### Event 2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0002    |
| Data Size    | 235 bytes |
| Instructions | 66        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       06 00 00 1E F0 FF  FF 7F 1D 00 80 23 24 01    ...........#$.
0010: 80 02 80 00 00 25 02 00  10 02 80 00 30 00 1D 03  .....%......0...
0020: 80 23 1D 04 80 23 3C 00  00 02 80 05 80 01 E4 00  .#...#<.........
0030: 02 00 10 05 80 00 4E 00  1D 06 80 23 1D 07 80 23  ......N....#...#
0040: 1D 08 80 23 3C 00 00 05  80 05 80 01 E4 00 02 00  ...#<...........
0050: 10 09 80 00 68 00 1D 0A  80 23 1D 0B 80 23 3C 00  ....h....#...#<.
0060: 00 09 80 05 80 01 E4 00  02 00 10 0C 80 00 82 00  ................
0070: 1D 0D 80 23 1D 0E 80 23  3C 00 00 0C 80 05 80 01  ...#...#<.......
0080: E4 00 02 00 10 0F 80 00  9C 00 1D 10 80 23 1D 11  .............#..
0090: 80 23 3C 00 00 0F 80 05  80 01 E4 00 02 00 10 12  .#<.............
00A0: 80 00 B2 00 1D 13 80 23  3C 00 00 12 80 05 80 01  .......#<.......
00B0: E4 00 02 00 10 14 80 00  D4 00 1D 15 80 23 1D 16  .............#..
00C0: 80 23 1D 17 80 23 1D 18  80 23 3C 00 00 14 80 05  .#...#...#<.....
00D0: 80 01 E4 00 02 00 10 19  80 00 E4 00 1D 1A 80 23  ...............#
00E0: 21 01 E4 00 1D 1B 80 23  01 0E 00 21 00           !......#...!.   
```

#### Opcodes

```
  0: 0x0002 [0x06] ExtData[1]->WorkLocal[0] = 0
  1: 0x0005 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=7168*)
    → "Welcome to the auction house. Do you have any questions about our establishment?"
  3: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000E [0x24] CREATE_DIALOG(message_id=7169*, default_option=0*, option_flags=ExtData[1]->WorkLocal[0])
    → "What do you want to know? [What is the auction house?/How are auctions run?/Are there any fees?/Are there any limits?/How do you check up on merchandise?/How do you remove an item?/My "Sales Status" list is full!/Nothing right now.]"
  5: 0x0015 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0016 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0030
  7: 0x001E [0x1D] PRINT_EVENT_MESSAGE(message_id=7170*)
    → "Auction houses can be found in all of Vana'diel's major cities. Here adventurers gather to bid on battle spoils, unwanted items, old armor...almost anything."
  8: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0022 [0x1D] PRINT_EVENT_MESSAGE(message_id=7172*)
    → "Adventurers may use any auction house regardless of nationality."
 10: 0x0025 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0026 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=0*, condition_work_offset=1*)
 12: 0x002D [0x01] GOTO 0x00E4
 13: 0x0030 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x004E
 14: 0x0038 [0x1D] PRINT_EVENT_MESSAGE(message_id=7173*)
    → "The first adventurer to bid at or above the asking price will automatically purchase the product."
 15: 0x003B [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x003C [0x1D] PRINT_EVENT_MESSAGE(message_id=7174*)
    → "Once put up for auction, merchandise will remain there for a maximum of thirty weeks Vana'diel time (nine-and-a-half days Earth time)."
 17: 0x003F [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0040 [0x1D] PRINT_EVENT_MESSAGE(message_id=7175*)
    → "If merchandise does not sell within this time limit, it will be returned to the seller's current residence."
 19: 0x0043 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0044 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=1*, condition_work_offset=1*)
 21: 0x004B [0x01] GOTO 0x00E4
 22: 0x004E [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0068
 23: 0x0056 [0x1D] PRINT_EVENT_MESSAGE(message_id=7176*)
    → "Transaction fees are proportional to the amount for which an item is put up on auction. The method of calculating this fee is different for single items and stackable items."
 24: 0x0059 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x005A [0x1D] PRINT_EVENT_MESSAGE(message_id=7177*)
    → "A transaction fee is collected when any merchandise is put up for auction. This fee is nonrefundable."
 26: 0x005D [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x005E [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=2*, condition_work_offset=1*)
 28: 0x0065 [0x01] GOTO 0x00E4
 29: 0x0068 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0082
 30: 0x0070 [0x1D] PRINT_EVENT_MESSAGE(message_id=7178*)
    → "The International Auction House Committee, or IAHC, has declared that a maximum of seven items may be put up for auction at one time."
 31: 0x0073 [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x0074 [0x1D] PRINT_EVENT_MESSAGE(message_id=7179*)
    → "However, the IAHC has recently removed the limit to how many items one may purchase."
 33: 0x0077 [0x23] WAIT_FOR_DIALOG_INTERACTION
 34: 0x0078 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=3*, condition_work_offset=1*)
 35: 0x007F [0x01] GOTO 0x00E4
 36: 0x0082 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x009C
 37: 0x008A [0x1D] PRINT_EVENT_MESSAGE(message_id=7180*)
    → "A small amount of time is required before new merchandise appears on our bid list."
 38: 0x008D [0x23] WAIT_FOR_DIALOG_INTERACTION
 39: 0x008E [0x1D] PRINT_EVENT_MESSAGE(message_id=7181*)
    → "Once an item appears on your "Sales Status" list, it may not immediately appear on the bid list. If you do not see your item on the bid list, try looking again at a later time."
 40: 0x0091 [0x23] WAIT_FOR_DIALOG_INTERACTION
 41: 0x0092 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=4*, condition_work_offset=1*)
 42: 0x0099 [0x01] GOTO 0x00E4
 43: 0x009C [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x00B2
 44: 0x00A4 [0x1D] PRINT_EVENT_MESSAGE(message_id=7182*)
    → "If you would like to withdraw an item from an auction, you must travel to the auction house, and select "Stop Sale" from the "Sales Status" menu."
 45: 0x00A7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 46: 0x00A8 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=5*, condition_work_offset=1*)
 47: 0x00AF [0x01] GOTO 0x00E4
 48: 0x00B2 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x00D4
 49: 0x00BA [0x1D] PRINT_EVENT_MESSAGE(message_id=7183*)
    → "To remove an item from your "Sales Status" list, you must visit an auction counter to acknowledge the sale or return of your merchandise."
 50: 0x00BD [0x23] WAIT_FOR_DIALOG_INTERACTION
 51: 0x00BE [0x1D] PRINT_EVENT_MESSAGE(message_id=7184*)
    → "Otherwise, previously sold or returned items will fill up your list and prevent you from selling any more merchandise."
 52: 0x00C1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 53: 0x00C2 [0x1D] PRINT_EVENT_MESSAGE(message_id=7185*)
    → "At any auction counter, open the "Sales Status" menu and acknowledge the transaction to clear it from the list."
 54: 0x00C5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 55: 0x00C6 [0x1D] PRINT_EVENT_MESSAGE(message_id=7186*)
    → "Press the confirm button to remove any transaction colored yellow (sold) or red (returned)."
 56: 0x00C9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 57: 0x00CA [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=6*, condition_work_offset=1*)
 58: 0x00D1 [0x01] GOTO 0x00E4
 59: 0x00D4 [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x00E4
 60: 0x00DC [0x1D] PRINT_EVENT_MESSAGE(message_id=7188*)
    → "In the past, many have amassed great wealth through the auction house. I hope you find fortune, too!"
 61: 0x00DF [0x23] WAIT_FOR_DIALOG_INTERACTION
 62: 0x00E0 [0x21] END_EVENT

SUBROUTINE_00E4:
 63: 0x00E4 [0x1D] PRINT_EVENT_MESSAGE(message_id=7187*)
    → "Is there anything else you would like to know?"
 64: 0x00E7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 65: 0x00E8 [0x01] GOTO 0x000E
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00E1 [0x01] GOTO 0x00E4
# Dead code (unreachable instructions):
     0x00EB [0x21] END_EVENT
     0x00EC [0x00] END_REQSTACK()
```
