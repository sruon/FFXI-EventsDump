# 17670743 - Moreno-Toeno

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Abyssea - Altepa (ID: 218) |
| Block Size       | 276 bytes                  |
| Total Events     | 6                          |
| References Count | 16                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [250](#event-250)     | 0x0001       |     45 |             19 |
| [251](#event-251)     | 0x002E       |     24 |              8 |
| [252](#event-252)     | 0x0046       |     43 |             12 |
| [253](#event-253)     | 0x0071       |     19 |              7 |
| [254](#event-254)     | 0x0084       |     39 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x1F30      |        7984 |
|       2 | 0x1F31      |        7985 |
|       3 | 0x1F32      |        7986 |
|       4 | 0x1F33      |        7987 |
|       5 | 0x1F34      |        7988 |
|       6 | 0x0B9F      |        2975 |
|       7 | 0x0003      |           3 |
|       8 | 0x1F35      |        7989 |
|       9 | 0x1F38      |        7992 |
|      10 | 0x1F36      |        7990 |
|      11 | 0x1F37      |        7991 |
|      12 | 0x00C9      |         201 |
|      13 | 0x0000      |           0 |
|      14 | 0x1F39      |        7993 |
|      15 | 0x1F3A      |        7994 |

## String References

- **7984**: Why, hello stranger. How would you like to assistaru me in a simple yet incalculably important task?
- **7985**: Allow me to elucidate. I am a teacher-weacher by trade, you see, but one with a pressing problem: I lack the teaching materials needed to properly impartaru knowledge to my pupils!
- **7986**: Our last experiment proved a bit too problematic for them. I must conduct it again, but cannot do so due to a paucity of pedagogical-wogical supplies.
- **7987**: Hm? Aren't there more importantaru matters to worry about, you say?
- **7988**: Preposterous! It is precisely-wisely because of our current predicament that education is as important as ever! How else will we raise a generation able to match wits with our foe and subsist in this severe environmentaru?
- **7989**: <Ahem> Where was I? Ah, yes. If you could retrieve $1 $0 for me, it would go a long way in helping-welping me achieve educational excellence. Think of the children!
- **7990**: Yes! This is just what I need to conductaru a review session for my students. However can I thank you?
- **7991**: Why, I know! Here, you can have this. If you ever find any more $0, don't hesitataru to bring them here. Remember, it's for a wonderful cause!
- **7992**: $1 $0 , I said. Didn't you learn how to take notes in school?
- **7993**: You wouldn't happen to have come across any more $0, by any chance? With a healthy supply, my students would be able to dive into their work without fear of failure. It's a key tenetaru of education, you know.
- **7994**: Wonderful! You've done a spectacular-wacular service for the young ones' future. Do stop by if you come across any more $0, will you?

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

### Event 250

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 45 bytes |
| Instructions | 19       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 1D 01 80 23 1D 02 80   ...........#...
0010: 23 1D 03 80 23 1D 04 80  23 1D 05 80 23 42 03 02  #...#...#...#B..
0020: 10 06 80 03 03 10 07 80  1D 08 80 23 21 00        ...........#!.  
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(20* ticks)
  2: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=7984*)
    → "Why, hello stranger. How would you like to assistaru me in a simple yet incalculably important task?"
  3: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000D [0x1D] PRINT_EVENT_MESSAGE(message_id=7985*)
    → "Allow me to elucidate. I am a teacher-weacher by trade, you see, but one with a pressing problem: I lack the teaching materials needed to properly impartaru knowledge to my pupils!"
  5: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0011 [0x1D] PRINT_EVENT_MESSAGE(message_id=7986*)
    → "Our last experiment proved a bit too problematic for them. I must conduct it again, but cannot do so due to a paucity of pedagogical-wogical supplies."
  7: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0015 [0x1D] PRINT_EVENT_MESSAGE(message_id=7987*)
    → "Hm? Aren't there more importantaru matters to worry about, you say?"
  9: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0019 [0x1D] PRINT_EVENT_MESSAGE(message_id=7988*)
    → "Preposterous! It is precisely-wisely because of our current predicament that education is as important as ever! How else will we raise a generation able to match wits with our foe and subsist in this severe environmentaru?"
 11: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x001D [0x42] SET_CLI_EVENT_CANCEL_DATA()
 13: 0x001E [0x03] Work_Zone[2] = 2975*
 14: 0x0023 [0x03] Work_Zone[3] = 3*
 15: 0x0028 [0x1D] PRINT_EVENT_MESSAGE(message_id=7989*)
    → "<Ahem> Where was I? Ah, yes. If you could retrieve $1 $0 for me, it would go a long way in helping-welping me achieve educational excellence. Think of the children!"
 16: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x002C [0x21] END_EVENT
 18: 0x002D [0x00] END_REQSTACK()
```

### Event 251

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 24 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            1E F0                ..
0030: FF FF 7F 1C 00 80 03 02  10 06 80 03 03 10 07 80  ................
0040: 1D 09 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x002E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0033 [0x1C] WAIT(20* ticks)
  2: 0x0036 [0x03] Work_Zone[2] = 2975*
  3: 0x003B [0x03] Work_Zone[3] = 3*
  4: 0x0040 [0x1D] PRINT_EVENT_MESSAGE(message_id=7992*)
    → "$1 $0 , I said. Didn't you learn how to take notes in school?"
  5: 0x0043 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0044 [0x21] END_EVENT
  7: 0x0045 [0x00] END_REQSTACK()
```

### Event 252

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 43 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   20 01  42 1E F0 FF FF 7F 1C 00         .B.......
0050: 80 1D 0A 80 23 03 02 10  06 80 1D 0B 80 23 45 0C  ....#........#E.
0060: 80 F0 FF FF 7F F0 FF FF  7F 71 73 74 63 0D 80 21  .........qstc..!
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x0046 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0048 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0049 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x004E [0x1C] WAIT(20* ticks)
  4: 0x0051 [0x1D] PRINT_EVENT_MESSAGE(message_id=7990*)
    → "Yes! This is just what I need to conductaru a review session for my students. However can I thank you?"
  5: 0x0054 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0055 [0x03] Work_Zone[2] = 2975*
  7: 0x005A [0x1D] PRINT_EVENT_MESSAGE(message_id=7991*)
    → "Why, I know! Here, you can have this. If you ever find any more $0, don't hesitataru to bring them here. Remember, it's for a wonderful cause!"
  8: 0x005D [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x005E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 10: 0x006F [0x21] END_EVENT
 11: 0x0070 [0x00] END_REQSTACK()
```

### Event 253

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0071   |
| Data Size    | 19 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    1E F0 FF FF 7F 1C 00  80 03 02 10 06 80 1D 0E   ...............
0080: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0071 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0076 [0x1C] WAIT(20* ticks)
  2: 0x0079 [0x03] Work_Zone[2] = 2975*
  3: 0x007E [0x1D] PRINT_EVENT_MESSAGE(message_id=7993*)
    → "You wouldn't happen to have come across any more $0, by any chance? With a healthy supply, my students would be able to dive into their work without fear of failure. It's a key tenetaru of education, you know."
  4: 0x0081 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0082 [0x21] END_EVENT
  6: 0x0083 [0x00] END_REQSTACK()
```

### Event 254

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0084   |
| Data Size    | 39 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             20 01 42 1E  F0 FF FF 7F 1C 00 80 03       .B.........
0090: 02 10 06 80 1D 0F 80 23  45 0C 80 F0 FF FF 7F F0  .......#E.......
00A0: FF FF 7F 71 73 74 63 0D  80 21 00                 ...qstc..!.     
```

#### Opcodes

```
  0: 0x0084 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0086 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0087 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x008C [0x1C] WAIT(20* ticks)
  4: 0x008F [0x03] Work_Zone[2] = 2975*
  5: 0x0094 [0x1D] PRINT_EVENT_MESSAGE(message_id=7994*)
    → "Wonderful! You've done a spectacular-wacular service for the young ones' future. Do stop by if you come across any more $0, will you?"
  6: 0x0097 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0098 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  8: 0x00A9 [0x21] END_EVENT
  9: 0x00AA [0x00] END_REQSTACK()
```
