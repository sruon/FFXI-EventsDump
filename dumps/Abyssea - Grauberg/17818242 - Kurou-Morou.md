# 17818242 - Kurou-Morou

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Abyssea - Grauberg (ID: 254) |
| Block Size       | 340 bytes                    |
| Total Events     | 4                            |
| References Count | 19                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [239](#event-239)     | 0x0001       |    163 |             44 |
| [240](#event-240)     | 0x00A4       |     37 |             11 |
| [242](#event-242)     | 0x00C9       |     29 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x001E      |          30 |
|       2 | 0x1FE6      |        8166 |
|       3 | 0x0028      |          40 |
|       4 | 0x1FE7      |        8167 |
|       5 | 0x1FE8      |        8168 |
|       6 | 0x1FE9      |        8169 |
|       7 | 0x1FEA      |        8170 |
|       8 | 0x1FF9      |        8185 |
|       9 | 0x1FFA      |        8186 |
|      10 | 0x0001      |           1 |
|      11 | 0x1FFC      |        8188 |
|      12 | 0x1FFB      |        8187 |
|      13 | 0x1FEB      |        8171 |
|      14 | 0x1FEC      |        8172 |
|      15 | 0x1FED      |        8173 |
|      16 | 0x1FEE      |        8174 |
|      17 | 0x1FEF      |        8175 |
|      18 | 0x1FF2      |        8178 |

## String References

- **8166**: Greetings! You stand before Kurou-Morou the Magnificentaru, from whose astrologically enlightened eyes naught can be concealed!
- **8167**: That doubt-laden gaze you bear... It is all too plainy-wain that you hold my talents and purpose in skepticism.
- **8168**: Many are the unbelievers who feel the revered art of fortune-telling is no longer relevantaru in our bedraggled world.
- **8169**: To them I say a big phooey-wooey, for it is precisely in this age of death and destruction that folk depend on the solace offered by clairvoyance!
- **8170**: Now, since I have taken a liking to you, I will divine for you your lucky item and lucky spot--absolutely-wutely free of charge!
- **8171**: Hrmmm! Your lucky item is... $0!
- **8172**: And your lucky spot is... [A place abundant in water/Someplace dark and cramped/A narrow pathway]!
- **8173**: With the specified lucky item in hand, seek out your designated lucky spot. In so doing, good fortune will surely visitaru you!
- **8174**: Your lucky item is $0!
- **8175**: And your lucky spot is [a place abundant in water/someplace dark and cramped/a narrow pathway]!
- **8178**: Hehehe, no need to say a word, friend. The cosmos has already revealed to me that good fortune has indeed visited you, in accordance-wordance with my divination. I trust you've learned not to doubtaru the significance of my talents.
- **8185**: Ah, so once again you come to Kurou-Morou the Magnificentaru, seeking a window into your future.
- **8186**: Request a fortune reading? [You read my mind!/Sorry, not interested.]
- **8187**: Tsk-tsk! Why do you insistaru on being untrue to yourself? Your insatiable hunger for the power of knowledge is plain to these eyes.
- **8188**: Very well, let the divination begin. As before, no paymentaru is required--serving the besty-west interests of the people is reward enough.

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

### Event 239

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 163 bytes |
| Instructions | 43        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 03 01 10 00 80 03  00 00 03 10 1E F0 FF FF   B..............
0010: 7F 1C 01 80 02 04 10 00  80 00 42 00 1D 02 80 23  ..........B....#
0020: 66 03 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 1D  f..........tlk0.
0030: 04 80 23 1D 05 80 23 1D  06 80 23 1D 07 80 23 01  ..#...#...#...#.
0040: 8C 00 1D 08 80 23 24 09  80 0A 80 00 80 25 02 00  .....#$......%..
0050: 10 00 80 00 6C 00 66 03  80 F8 FF FF 7F F8 FF FF  ....l.f.........
0060: 7F 74 6C 6B 30 1D 0B 80  23 01 8C 00 02 00 10 0A  .tlk0...#.......
0070: 80 00 8C 00 66 03 80 F8  FF FF 7F F8 FF FF 7F 74  ....f..........t
0080: 6C 6B 30 1D 0C 80 23 21  00 01 8C 00 1D 0D 80 23  lk0...#!.......#
0090: 03 03 10 00 00 1D 0E 80  23 1D 0F 80 23 03 01 10  ........#...#...
00A0: 0A 80 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x03] Work_Zone[1] = 0*
  2: 0x0007 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
  3: 0x000C [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0011 [0x1C] WAIT(30* ticks)
  5: 0x0014 [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x0042
  6: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=8166*)
    → "Greetings! You stand before Kurou-Morou the Magnificentaru, from whose astrologically enlightened eyes naught can be concealed!"
  7: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0020 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  9: 0x002F [0x1D] PRINT_EVENT_MESSAGE(message_id=8167*)
    → "That doubt-laden gaze you bear... It is all too plainy-wain that you hold my talents and purpose in skepticism."
 10: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0033 [0x1D] PRINT_EVENT_MESSAGE(message_id=8168*)
    → "Many are the unbelievers who feel the revered art of fortune-telling is no longer relevantaru in our bedraggled world."
 12: 0x0036 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0037 [0x1D] PRINT_EVENT_MESSAGE(message_id=8169*)
    → "To them I say a big phooey-wooey, for it is precisely in this age of death and destruction that folk depend on the solace offered by clairvoyance!"
 14: 0x003A [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x003B [0x1D] PRINT_EVENT_MESSAGE(message_id=8170*)
    → "Now, since I have taken a liking to you, I will divine for you your lucky item and lucky spot--absolutely-wutely free of charge!"
 16: 0x003E [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x003F [0x01] GOTO 0x008C
 18: 0x0042 [0x1D] PRINT_EVENT_MESSAGE(message_id=8185*)
    → "Ah, so once again you come to Kurou-Morou the Magnificentaru, seeking a window into your future."
 19: 0x0045 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0046 [0x24] CREATE_DIALOG(message_id=8186*, default_option=1*, option_flags=0*)
    → "Request a fortune reading? [You read my mind!/Sorry, not interested.]"
 21: 0x004D [0x25] WAIT_DIALOG_SELECT()
 22: 0x004E [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x006C
 23: 0x0056 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
 24: 0x0065 [0x1D] PRINT_EVENT_MESSAGE(message_id=8188*)
    → "Very well, let the divination begin. As before, no paymentaru is required--serving the besty-west interests of the people is reward enough."
 25: 0x0068 [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x0069 [0x01] GOTO 0x008C
 27: 0x006C [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x008C
 28: 0x0074 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
 29: 0x0083 [0x1D] PRINT_EVENT_MESSAGE(message_id=8187*)
    → "Tsk-tsk! Why do you insistaru on being untrue to yourself? Your insatiable hunger for the power of knowledge is plain to these eyes."
 30: 0x0086 [0x23] WAIT_FOR_DIALOG_INTERACTION
 31: 0x0087 [0x21] END_EVENT
 32: 0x0088 [0x00] END_REQSTACK()

SUBROUTINE_008C:
 33: 0x008C [0x1D] PRINT_EVENT_MESSAGE(message_id=8171*)
    → "Hrmmm! Your lucky item is... $0!"
 34: 0x008F [0x23] WAIT_FOR_DIALOG_INTERACTION
 35: 0x0090 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[0]
 36: 0x0095 [0x1D] PRINT_EVENT_MESSAGE(message_id=8172*)
    → "And your lucky spot is... [A place abundant in water/Someplace dark and cramped/A narrow pathway]!"
 37: 0x0098 [0x23] WAIT_FOR_DIALOG_INTERACTION
 38: 0x0099 [0x1D] PRINT_EVENT_MESSAGE(message_id=8173*)
    → "With the specified lucky item in hand, seek out your designated lucky spot. In so doing, good fortune will surely visitaru you!"
 39: 0x009C [0x23] WAIT_FOR_DIALOG_INTERACTION
 40: 0x009D [0x03] Work_Zone[1] = 1*
 41: 0x00A2 [0x21] END_EVENT
 42: 0x00A3 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0089 [0x01] GOTO 0x008C
```

### Event 240

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A4   |
| Data Size    | 37 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:             1E F0 FF FF  7F 1C 01 80 66 03 80 F8      ........f...
00B0: FF FF 7F F8 FF FF 7F 74  6C 6B 30 1D 10 80 23 1D  .......tlk0...#.
00C0: 11 80 23 1D 0F 80 23 21  00                       ..#...#!.       
```

#### Opcodes

```
  0: 0x00A4 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00A9 [0x1C] WAIT(30* ticks)
  2: 0x00AC [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  3: 0x00BB [0x1D] PRINT_EVENT_MESSAGE(message_id=8174*)
    → "Your lucky item is $0!"
  4: 0x00BE [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00BF [0x1D] PRINT_EVENT_MESSAGE(message_id=8175*)
    → "And your lucky spot is [a place abundant in water/someplace dark and cramped/a narrow pathway]!"
  6: 0x00C2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00C3 [0x1D] PRINT_EVENT_MESSAGE(message_id=8173*)
    → "With the specified lucky item in hand, seek out your designated lucky spot. In so doing, good fortune will surely visitaru you!"
  8: 0x00C6 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x00C7 [0x21] END_EVENT
 10: 0x00C8 [0x00] END_REQSTACK()
```

### Event 242

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C9   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                             1E F0 FF FF 7F 1C 01           .......
00D0: 80 66 03 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  .f..........tlk0
00E0: 1D 12 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x00C9 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00CE [0x1C] WAIT(30* ticks)
  2: 0x00D1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  3: 0x00E0 [0x1D] PRINT_EVENT_MESSAGE(message_id=8178*)
    → "Hehehe, no need to say a word, friend. The cosmos has already revealed to me that good fortune has indeed visited you, in accordance-wordance with my divination. I trust you've learned not to doubtaru the significance of my talents."
  4: 0x00E3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00E4 [0x21] END_EVENT
  6: 0x00E5 [0x00] END_REQSTACK()
```
