# 17867265 - Grrk-Frut the Charlatan

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Marjami Ravine (ID: 266) |
| Block Size       | 344 bytes                |
| Total Events     | 4                        |
| References Count | 24                       |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [59](#event-59)       | 0x0001       |    110 |             35 |
| [60](#event-60)       | 0x006F       |     19 |              7 |
| [61](#event-61)       | 0x0082       |     83 |             27 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x200F      |        8207 |
|       2 | 0x2010      |        8208 |
|       3 | 0x2011      |        8209 |
|       4 | 0x0000      |           0 |
|       5 | 0x2012      |        8210 |
|       6 | 0x0101      |         257 |
|       7 | 0x00E6      |         230 |
|       8 | 0x2013      |        8211 |
|       9 | 0x2014      |        8212 |
|      10 | 0x0014      |          20 |
|      11 | 0x2015      |        8213 |
|      12 | 0x2016      |        8214 |
|      13 | 0x2017      |        8215 |
|      14 | 0x2018      |        8216 |
|      15 | 0x0006      |           6 |
|      16 | 0x200D      |        8205 |
|      17 | 0x2007      |        8199 |
|      18 | 0x2008      |        8200 |
|      19 | 0x2009      |        8201 |
|      20 | 0x200A      |        8202 |
|      21 | 0x200B      |        8203 |
|      22 | 0x200C      |        8204 |
|      23 | 0x200E      |        8206 |

## String References

- **8199**: Altana-child, I have story for you. Come. Listen.
- **8200**: Listen to his story? [Sure, I've got time./I don't trust him.]
- **8201**: Guk guk guk! Our special item no good for Altana-child. Get bad curse. Very not safe.
- **8202**: Curse haunt you always. Can't avoid.
- **8203**: Make you kick bucket if touch. Bad.
- **8204**: You look strong. Find and bring to me. I help you.
- **8205**: Bring me $0.
- **8206**: Guk guk guk! You come back. I know.
- **8207**: Guk guk guk. You bring stuff? Lucky be alive.
- **8208**: Give to me. I rid you curse.
- **8209**: Hand over the goods? [If you say so./Finders keepers.]
- **8210**: I clear curse now.
- **8211**: You receive a blessing.
- **8212**: Curse gone. You lucky. Find more and bring. I clear again. Guk guk guk!
- **8213**: Guk guk guk... You no realize yet?
- **8214**: We have many now. Very strong.
- **8215**: I no need you. But I take anyway. Guk guk guk!
- **8216**: Guk guk guk! If you want be curse, I no stop.

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

### Event 59

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 110 bytes |
| Instructions | 35        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 1D 01 80 23 1D 02 80   ...........#...
0010: 23 24 03 80 00 80 04 80  25 02 00 10 04 80 00 58  #$......%......X
0020: 00 42 1D 05 80 23 73 06  80 F8 FF FF 7F F0 FF FF  .B...#s.........
0030: 7F 1C 07 80 48 08 80 23  1D 09 80 23 02 02 10 0A  ....H..#...#....
0040: 80 04 50 00 1D 0B 80 23  1D 0C 80 23 1D 0D 80 23  ..P....#...#...#
0050: 03 01 10 04 80 01 6C 00  02 00 10 00 80 00 6C 00  ......l.......l.
0060: 1D 0E 80 23 03 01 10 00  80 01 6C 00 2E 21 00     ...#......l..!. 
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(1* ticks)
  2: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=8207*)
    → "Guk guk guk. You bring stuff? Lucky be alive."
  3: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000D [0x1D] PRINT_EVENT_MESSAGE(message_id=8208*)
    → "Give to me. I rid you curse."
  5: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0011 [0x24] CREATE_DIALOG(message_id=8209*, default_option=1*, option_flags=0*)
    → "Hand over the goods? [If you say so./Finders keepers.]"
  7: 0x0018 [0x25] WAIT_DIALOG_SELECT()
  8: 0x0019 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0058
  9: 0x0021 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 10: 0x0022 [0x1D] PRINT_EVENT_MESSAGE(message_id=8210*)
    → "I clear curse now."
 11: 0x0025 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0026 [0x73] EventEntity casts magic 257* on LocalPlayer
 13: 0x0031 [0x1C] WAIT(230* ticks)
 14: 0x0034 [0x48] [System] [8211*]:
    → "You receive a blessing."
 15: 0x0037 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0038 [0x1D] PRINT_EVENT_MESSAGE(message_id=8212*)
    → "Curse gone. You lucky. Find more and bring. I clear again. Guk guk guk!"
 17: 0x003B [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x003C [0x02] IF !(Work_Zone[2] < 20*) GOTO 0x0050
 19: 0x0044 [0x1D] PRINT_EVENT_MESSAGE(message_id=8213*)
    → "Guk guk guk... You no realize yet?"
 20: 0x0047 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0048 [0x1D] PRINT_EVENT_MESSAGE(message_id=8214*)
    → "We have many now. Very strong."
 22: 0x004B [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x004C [0x1D] PRINT_EVENT_MESSAGE(message_id=8215*)
    → "I no need you. But I take anyway. Guk guk guk!"
 24: 0x004F [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x0050 [0x03] Work_Zone[1] = 0*
 26: 0x0055 [0x01] GOTO 0x006C
 27: 0x0058 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x006C
 28: 0x0060 [0x1D] PRINT_EVENT_MESSAGE(message_id=8216*)
    → "Guk guk guk! If you want be curse, I no stop."
 29: 0x0063 [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x0064 [0x03] Work_Zone[1] = 1*
 31: 0x0069 [0x01] GOTO 0x006C

SUBROUTINE_006C:
 32: 0x006C [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 33: 0x006D [0x21] END_EVENT
 34: 0x006E [0x00] END_REQSTACK()
```

### Event 60

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006F   |
| Data Size    | 19 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                               1E                 .
0070: F0 FF FF 7F 1C 00 80 03  02 10 0F 80 1D 10 80 23  ...............#
0080: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x006F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0074 [0x1C] WAIT(1* ticks)
  2: 0x0077 [0x03] Work_Zone[2] = 6*
  3: 0x007C [0x1D] PRINT_EVENT_MESSAGE(message_id=8205*)
    → "Bring me $0."
  4: 0x007F [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0080 [0x21] END_EVENT
  6: 0x0081 [0x00] END_REQSTACK()
```

### Event 61

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0082   |
| Data Size    | 83 bytes |
| Instructions | 27       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:       1E F0 FF FF 7F 1C  00 80 1D 11 80 23 24 12    ...........#$.
0090: 80 04 80 04 80 25 02 00  10 04 80 00 BF 00 1D 13  .....%..........
00A0: 80 23 1D 14 80 23 1D 15  80 23 1D 16 80 23 03 02  .#...#...#...#..
00B0: 10 0F 80 1D 10 80 23 03  01 10 04 80 01 D3 00 02  ......#.........
00C0: 00 10 00 80 00 D3 00 1D  17 80 23 03 01 10 00 80  ..........#.....
00D0: 01 D3 00 21 00                                    ...!.           
```

#### Opcodes

```
  0: 0x0082 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0087 [0x1C] WAIT(1* ticks)
  2: 0x008A [0x1D] PRINT_EVENT_MESSAGE(message_id=8199*)
    → "Altana-child, I have story for you. Come. Listen."
  3: 0x008D [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x008E [0x24] CREATE_DIALOG(message_id=8200*, default_option=0*, option_flags=0*)
    → "Listen to his story? [Sure, I've got time./I don't trust him.]"
  5: 0x0095 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0096 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00BF
  7: 0x009E [0x1D] PRINT_EVENT_MESSAGE(message_id=8201*)
    → "Guk guk guk! Our special item no good for Altana-child. Get bad curse. Very not safe."
  8: 0x00A1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x00A2 [0x1D] PRINT_EVENT_MESSAGE(message_id=8202*)
    → "Curse haunt you always. Can't avoid."
 10: 0x00A5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x00A6 [0x1D] PRINT_EVENT_MESSAGE(message_id=8203*)
    → "Make you kick bucket if touch. Bad."
 12: 0x00A9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x00AA [0x1D] PRINT_EVENT_MESSAGE(message_id=8204*)
    → "You look strong. Find and bring to me. I help you."
 14: 0x00AD [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x00AE [0x03] Work_Zone[2] = 6*
 16: 0x00B3 [0x1D] PRINT_EVENT_MESSAGE(message_id=8205*)
    → "Bring me $0."
 17: 0x00B6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x00B7 [0x03] Work_Zone[1] = 0*
 19: 0x00BC [0x01] GOTO 0x00D3
 20: 0x00BF [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00D3
 21: 0x00C7 [0x1D] PRINT_EVENT_MESSAGE(message_id=8206*)
    → "Guk guk guk! You come back. I know."
 22: 0x00CA [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x00CB [0x03] Work_Zone[1] = 1*
 24: 0x00D0 [0x01] GOTO 0x00D3

SUBROUTINE_00D3:
 25: 0x00D3 [0x21] END_EVENT
 26: 0x00D4 [0x00] END_REQSTACK()
```
