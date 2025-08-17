# 17801274 - Hari Pakhroib

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Kazham (ID: 250) |
| Block Size       | 532 bytes        |
| Total Events     | 15               |
| References Count | 26               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [84](#event-84)          | 0x001A       |     33 |             12 |
| [175](#event-175)        | 0x003B       |     33 |             12 |
| [68](#event-68)          | 0x005C       |     91 |             22 |
| [65535.3](#event-655353) | 0x00B7       |      9 |              5 |
| [65535.4](#event-655354) | 0x00C0       |      9 |              5 |
| [65535.5](#event-655355) | 0x00C9       |      9 |              5 |
| [65535.6](#event-655356) | 0x00D2       |      9 |              5 |
| [65535.7](#event-655357) | 0x00DB       |      5 |              3 |
| [65535.8](#event-655358) | 0x00E0       |      5 |              3 |
| [69](#event-69)          | 0x00E5       |     33 |             12 |
| [71](#event-71)          | 0x0106       |     58 |             15 |
| [72](#event-72)          | 0x0140       |     29 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x001E      |          30 |
|       2 | 0x271A      |       10010 |
|       3 | 0x271B      |       10011 |
|       4 | 0x2872      |       10354 |
|       5 | 0x2873      |       10355 |
|       6 | 0x273E      |       10046 |
|       7 | 0x0000      |           0 |
|       8 | 0x0001      |           1 |
|       9 | 0x2744      |       10052 |
|      10 | 0x0002      |           2 |
|      11 | 0x273A      |       10042 |
|      12 | 0x273B      |       10043 |
|      13 | 0x273C      |       10044 |
|      14 | 0x273D      |       10045 |
|      15 | 0x273F      |       10047 |
|      16 | 0x2740      |       10048 |
|      17 | 0x2741      |       10049 |
|      18 | 0x2742      |       10050 |
|      19 | 0x2743      |       10051 |
|      20 | 0x2745      |       10053 |
|      21 | 0x2746      |       10054 |
|      22 | 0x2749      |       10057 |
|      23 | 0x274A      |       10058 |
|      24 | 0x00C9      |         201 |
|      25 | 0x274B      |       10059 |

## String References

- **10010**: Hey therrre, adventurer! Have you got your fill of Kazham?
- **10011**: What about that volcano to the east of herrre? Bet you haven't been therrre yet, have you?
- **10042**: Kazham is protected by the guardian of the volcano located east of herrre. With his laughter and anger, the guardian shakes the earth and grants us the strrrength to survive.
- **10043**: To show our thanks every day, we take the guardian offerings of our best crops. This is how it has been for hundreds of yearrrs.
- **10044**: It doesn't look like you're doing much more than being in the way. How about taking a trip to the volcano and showing your face to our guarrrdian?
- **10045**: If you're lucky, you might even hear his rrroar! Hah-hah-hah!
- **10046**: So, are you going to make yourself useful? [Count me in./I'm busy.]
- **10047**: That's the spirit. Today's offering is $1.
- **10048**: What? Did you think I was going to provide you one for frrree? What good is an offering of thanks if it isn't YOU who's showing the thanks?
- **10049**: Now listen up. Enter the volcano and journey up to the crrrater. There you will find an altar that we made.
- **10050**: After you've placed the $1 on the altar, you must shout your name into the crater so the guardian of our land can hearrr.
- **10051**: Oh, and you should probably take a couple $2 with you. You never know when you will need them.
- **10052**: Well, if that's the case, why don't you just take the next airship and get off of our island?
- **10053**: Travel east to the towerrring volcano. Walk up to the crater and place $1 on the altar therrre. Oh, and don't forget to shout your name.
- **10054**: And shout it like you mean it. If your voice is heard by our guarrrdian, then your stay on our island should be a safe one.
- **10057**: Oh, you made it back in one piece! You look a lot tougher now than you did beforrre you left.
- **10058**: We Mithra like our [men/women] strong and brave like you. Here, take this.
- **10059**: No matter who or what you are, without strength, you'll make no impression on this worrrld.
- **10354**: Hey there, adventurerrr! Have you got you got your fill of Kazham?
- **10355**: If you have, get out alrrready. You stink!

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    5E 69 64 6C 30 1C 01  80 00                     ^idl0....      
```

#### Opcodes

```
  0: 0x0011 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0016 [0x1C] WAIT(30* ticks)
  2: 0x0019 [0x00] END_REQSTACK()
```

### Event 84

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                1E F0 FF FF 7F 6F            .....o
0020: 70 29 08 3A A0 0F 01 01  1D 02 80 23 1D 03 80 23  p).:.......#...#
0030: 29 08 3A A0 0F 01 02 20  00 21 00                 ).:.... .!.     
```

#### Opcodes

```
  0: 0x001A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0020 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0021 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hari Pakhroib (ID: 17801274/0x010FA03A), tag_num=0x01)
  4: 0x0028 [0x1D] PRINT_EVENT_MESSAGE(message_id=10010*)
    → "Hey therrre, adventurer! Have you got your fill of Kazham?"
  5: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x002C [0x1D] PRINT_EVENT_MESSAGE(message_id=10011*)
    → "What about that volcano to the east of herrre? Bet you haven't been therrre yet, have you?"
  7: 0x002F [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0030 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hari Pakhroib (ID: 17801274/0x010FA03A), tag_num=0x02)
  9: 0x0037 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0039 [0x21] END_EVENT
 11: 0x003A [0x00] END_REQSTACK()
```

### Event 175

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   1E F0 FF FF 7F             .....
0040: 6F 70 29 08 3A A0 0F 01  01 1D 04 80 23 1D 05 80  op).:.......#...
0050: 23 29 08 3A A0 0F 01 02  20 00 21 00              #).:.... .!.    
```

#### Opcodes

```
  0: 0x003B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0040 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0041 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0042 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hari Pakhroib (ID: 17801274/0x010FA03A), tag_num=0x01)
  4: 0x0049 [0x1D] PRINT_EVENT_MESSAGE(message_id=10354*)
    → "Hey there, adventurerrr! Have you got you got your fill of Kazham?"
  5: 0x004C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x004D [0x1D] PRINT_EVENT_MESSAGE(message_id=10355*)
    → "If you have, get out alrrready. You stink!"
  7: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0051 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hari Pakhroib (ID: 17801274/0x010FA03A), tag_num=0x02)
  9: 0x0058 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x005A [0x21] END_EVENT
 11: 0x005B [0x00] END_REQSTACK()
```

### Event 68

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005C   |
| Data Size    | 91 bytes |
| Instructions | 22       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      1E F0 FF FF              ....
0060: 7F 6F 70 29 0B 3A A0 0F  01 06 29 0B 3A A0 0F 01  .op).:....).:...
0070: 07 24 06 80 07 80 07 80  25 02 00 10 07 80 00 9F  .$......%.......
0080: 00 42 03 01 10 08 80 29  0B 3A A0 0F 01 08 29 0B  .B.....).:....).
0090: 3A A0 0F 01 09 29 0B 3A  A0 0F 01 0A 01 B3 00 02  :....).:........
00A0: 00 10 08 80 00 B3 00 1D  09 80 23 03 01 10 0A 80  ..........#.....
00B0: 01 B3 00 20 00 21 00                              ... .!.         
```

#### Opcodes

```
  0: 0x005C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0061 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0062 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0063 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Hari Pakhroib (ID: 17801274/0x010FA03A), tag_num=0x06)
  4: 0x006A [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Hari Pakhroib (ID: 17801274/0x010FA03A), tag_num=0x07)
  5: 0x0071 [0x24] CREATE_DIALOG(message_id=10046*, default_option=0*, option_flags=0*)
    → "So, are you going to make yourself useful? [Count me in./I'm busy.]"
  6: 0x0078 [0x25] WAIT_DIALOG_SELECT()
  7: 0x0079 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x009F
  8: 0x0081 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  9: 0x0082 [0x03] Work_Zone[1] = 1*
 10: 0x0087 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Hari Pakhroib (ID: 17801274/0x010FA03A), tag_num=0x08)
 11: 0x008E [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Hari Pakhroib (ID: 17801274/0x010FA03A), tag_num=0x09)
 12: 0x0095 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Hari Pakhroib (ID: 17801274/0x010FA03A), tag_num=0x0A)
 13: 0x009C [0x01] GOTO 0x00B3
 14: 0x009F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00B3
 15: 0x00A7 [0x1D] PRINT_EVENT_MESSAGE(message_id=10052*)
    → "Well, if that's the case, why don't you just take the next airship and get off of our island?"
 16: 0x00AA [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x00AB [0x03] Work_Zone[1] = 2*
 18: 0x00B0 [0x01] GOTO 0x00B3

SUBROUTINE_00B3:
 19: 0x00B3 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 20: 0x00B5 [0x21] END_EVENT
 21: 0x00B6 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B7  |
| Data Size    | 9 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                      1D  0B 80 23 1D 0C 80 23 00         ...#...#.
```

#### Opcodes

```
  0: 0x00B7 [0x1D] PRINT_EVENT_MESSAGE(message_id=10042*)
    → "Kazham is protected by the guardian of the volcano located east of herrre. With his laughter and anger, the guardian shakes the earth and grants us the strrrength to survive."
  1: 0x00BA [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00BB [0x1D] PRINT_EVENT_MESSAGE(message_id=10043*)
    → "To show our thanks every day, we take the guardian offerings of our best crops. This is how it has been for hundreds of yearrrs."
  3: 0x00BE [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x00BF [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C0  |
| Data Size    | 9 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0: 1D 0D 80 23 1D 0E 80 23  00                       ...#...#.       
```

#### Opcodes

```
  0: 0x00C0 [0x1D] PRINT_EVENT_MESSAGE(message_id=10044*)
    → "It doesn't look like you're doing much more than being in the way. How about taking a trip to the volcano and showing your face to our guarrrdian?"
  1: 0x00C3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00C4 [0x1D] PRINT_EVENT_MESSAGE(message_id=10045*)
    → "If you're lucky, you might even hear his rrroar! Hah-hah-hah!"
  3: 0x00C7 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x00C8 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C9  |
| Data Size    | 9 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                             1D 0F 80 23 1D 10 80           ...#...
00D0: 23 00                                             #.              
```

#### Opcodes

```
  0: 0x00C9 [0x1D] PRINT_EVENT_MESSAGE(message_id=10047*)
    → "That's the spirit. Today's offering is $1."
  1: 0x00CC [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00CD [0x1D] PRINT_EVENT_MESSAGE(message_id=10048*)
    → "What? Did you think I was going to provide you one for frrree? What good is an offering of thanks if it isn't YOU who's showing the thanks?"
  3: 0x00D0 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x00D1 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00D2  |
| Data Size    | 9 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:       1D 11 80 23 1D 12  80 23 00                   ...#...#.     
```

#### Opcodes

```
  0: 0x00D2 [0x1D] PRINT_EVENT_MESSAGE(message_id=10049*)
    → "Now listen up. Enter the volcano and journey up to the crrrater. There you will find an altar that we made."
  1: 0x00D5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00D6 [0x1D] PRINT_EVENT_MESSAGE(message_id=10050*)
    → "After you've placed the $1 on the altar, you must shout your name into the crater so the guardian of our land can hearrr."
  3: 0x00D9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x00DA [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00DB  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                   1D 13 80 23 00             ...#.
```

#### Opcodes

```
  0: 0x00DB [0x1D] PRINT_EVENT_MESSAGE(message_id=10051*)
    → "Oh, and you should probably take a couple $2 with you. You never know when you will need them."
  1: 0x00DE [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00DF [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00E0  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0: 1D 09 80 23 00                                    ...#.           
```

#### Opcodes

```
  0: 0x00E0 [0x1D] PRINT_EVENT_MESSAGE(message_id=10052*)
    → "Well, if that's the case, why don't you just take the next airship and get off of our island?"
  1: 0x00E3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00E4 [0x00] END_REQSTACK()
```

### Event 69

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E5   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                1E F0 FF  FF 7F 6F 70 29 08 3A A0       .....op).:.
00F0: 0F 01 01 1D 14 80 23 1D  15 80 23 29 08 3A A0 0F  ......#...#).:..
0100: 01 02 20 00 21 00                                 .. .!.          
```

#### Opcodes

```
  0: 0x00E5 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00EA [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00EB [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00EC [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hari Pakhroib (ID: 17801274/0x010FA03A), tag_num=0x01)
  4: 0x00F3 [0x1D] PRINT_EVENT_MESSAGE(message_id=10053*)
    → "Travel east to the towerrring volcano. Walk up to the crater and place $1 on the altar therrre. Oh, and don't forget to shout your name."
  5: 0x00F6 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00F7 [0x1D] PRINT_EVENT_MESSAGE(message_id=10054*)
    → "And shout it like you mean it. If your voice is heard by our guarrrdian, then your stay on our island should be a safe one."
  7: 0x00FA [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00FB [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hari Pakhroib (ID: 17801274/0x010FA03A), tag_num=0x02)
  9: 0x0102 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0104 [0x21] END_EVENT
 11: 0x0105 [0x00] END_REQSTACK()
```

### Event 71

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0106   |
| Data Size    | 58 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                   42 29  08 F0 FF FF 7F 03 1E F0        B)........
0110: FF FF 7F 6F 70 29 08 3A  A0 0F 01 01 1D 16 80 23  ...op).:.......#
0120: 1D 17 80 23 29 08 3A A0  0F 01 02 45 18 80 F0 FF  ...#).:....E....
0130: FF 7F F0 FF FF 7F 71 73  74 63 07 80 20 00 21 00  ......qstc.. .!.
```

#### Opcodes

```
  0: 0x0106 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0107 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=LocalPlayer, tag_num=0x03)
  2: 0x010E [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0113 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0114 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x0115 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hari Pakhroib (ID: 17801274/0x010FA03A), tag_num=0x01)
  6: 0x011C [0x1D] PRINT_EVENT_MESSAGE(message_id=10057*)
    → "Oh, you made it back in one piece! You look a lot tougher now than you did beforrre you left."
  7: 0x011F [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0120 [0x1D] PRINT_EVENT_MESSAGE(message_id=10058*)
    → "We Mithra like our [men/women] strong and brave like you. Here, take this."
  9: 0x0123 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0124 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hari Pakhroib (ID: 17801274/0x010FA03A), tag_num=0x02)
 11: 0x012B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 12: 0x013C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 13: 0x013E [0x21] END_EVENT
 14: 0x013F [0x00] END_REQSTACK()
```

### Event 72

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0140   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140: 1E F0 FF FF 7F 6F 70 29  08 3A A0 0F 01 01 1D 19  .....op).:......
0150: 80 23 29 08 3A A0 0F 01  02 20 00 21 00           .#).:.... .!.   
```

#### Opcodes

```
  0: 0x0140 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0145 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0146 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0147 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hari Pakhroib (ID: 17801274/0x010FA03A), tag_num=0x01)
  4: 0x014E [0x1D] PRINT_EVENT_MESSAGE(message_id=10059*)
    → "No matter who or what you are, without strength, you'll make no impression on this worrrld."
  5: 0x0151 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0152 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hari Pakhroib (ID: 17801274/0x010FA03A), tag_num=0x02)
  7: 0x0159 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x015B [0x21] END_EVENT
  9: 0x015C [0x00] END_REQSTACK()
```
