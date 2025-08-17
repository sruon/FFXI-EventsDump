# 17727559 - Arminibit

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Port San d'Oria (ID: 232) |
| Block Size       | 636 bytes                 |
| Total Events     | 21                        |
| References Count | 26                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [24](#event-24)          | 0x0001       |    139 |             27 |
| [18](#event-18)          | 0x008C       |      1 |              1 |
| [5](#event-5)            | 0x008D       |     15 |              5 |
| [17](#event-17)          | 0x009C       |      1 |              1 |
| [0](#event-0)            | 0x009D       |     15 |              5 |
| [1](#event-1)            | 0x00AC       |     15 |              5 |
| [2](#event-2)            | 0x00BB       |     15 |              5 |
| [7](#event-7)            | 0x00CA       |      1 |              1 |
| [19](#event-19)          | 0x00CB       |      1 |              1 |
| [15](#event-15)          | 0x00CC       |      1 |              1 |
| [22](#event-22)          | 0x00CD       |      1 |              1 |
| [586](#event-586)        | 0x00CE       |     63 |             15 |
| [65535.1](#event-655351) | 0x010D       |     10 |              2 |
| [65535.2](#event-655352) | 0x0117       |     20 |              6 |
| [65535.3](#event-655353) | 0x012B       |     22 |              8 |
| [65535.4](#event-655354) | 0x0141       |     19 |              3 |
| [65535.5](#event-655355) | 0x0154       |      9 |              3 |
| [65535.6](#event-655356) | 0x015D       |     19 |              3 |
| [65535.7](#event-655357) | 0x0170       |     32 |              4 |
| [65535.8](#event-655358) | 0x0190       |     29 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x208C      |        8332 |
|       1 | 0x0014      |          20 |
|       2 | 0x208D      |        8333 |
|       3 | 0x208E      |        8334 |
|       4 | 0x208F      |        8335 |
|       5 | 0x2090      |        8336 |
|       6 | 0x2091      |        8337 |
|       7 | 0x2092      |        8338 |
|       8 | 0x20A8      |        8360 |
|       9 | 0x20B8      |        8376 |
|      10 | 0x20EB      |        8427 |
|      11 | 0x20FA      |        8442 |
|      12 | 0x1ECC      |        7884 |
|      13 | 0x003C      |          60 |
|      14 | 0x1ECD      |        7885 |
|      15 | 0x001E      |          30 |
|      16 | 0xFFFFFC88  |  4294966408 |
|      17 | 0xFFFE43E2  |  4294853602 |
|      18 | 0xFFFFF060  |  4294963296 |
|      19 | 0x0CFB      |        3323 |
|      20 | 0x000D      |          13 |
|      21 | 0x0273      |         627 |
|      22 | 0xFFFE55A7  |  4294858151 |
|      23 | 0x07ED      |        2029 |
|      24 | 0xFFFE274C  |  4294846284 |
|      25 | 0xFFFFE0C0  |  4294959296 |

## String References

- **7884**: I've told Fontoumant, so all you have to do is deliver the goods to Avandale as...
- **7885**: Hey! There're some things best left unheard, stranger. I trust you'll be leaving... Now!

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

### Event 24

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 139 bytes |
| Instructions | 27        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 4A 47 80 0E 01 48  80 0E 01 2B 47 80 0E 01   BJG...H...+G...
0010: 00 80 23 6F 76 47 80 0E  01 4A 48 80 0E 01 47 80  ..#ovG...JH...G.
0020: 0E 01 6F 76 48 80 0E 01  66 01 80 48 80 0E 01 48  ..ovH...f..H...H
0030: 80 0E 01 74 68 6B 31 2B  48 80 0E 01 02 80 23 66  ...thk1+H.....#f
0040: 01 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 2B 47  ..........tlk0+G
0050: 80 0E 01 03 80 23 2B 47  80 0E 01 04 80 23 5E 69  .....#+G.....#^i
0060: 64 6C 30 66 01 80 48 80  0E 01 48 80 0E 01 74 68  dl0f..H...H...th
0070: 6B 32 2B 48 80 0E 01 05  80 23 2B 47 80 0E 01 06  k2+H.....#+G....
0080: 80 23 2B 48 80 0E 01 07  80 23 21 00              .#+H.....#!.    
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x4A] Arminibit (ID: 17727559/0x010E8047) looks at Ceraulian (ID: 17727560/0x010E8048)
  2: 0x000B [0x2B] Arminibit (ID: 17727559/0x010E8047) [8332*]:
    → "You hear more and more talk of the Dragon King Ranperre these days. They say that his top vassal was a dragoon. I wonder what ever happened to all the dragoons..."
  3: 0x0012 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0013 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0014 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Arminibit (ID: 17727559/0x010E8047) Render.Flags0 and Render.Flags3 conditions are met
  6: 0x0019 [0x4A] Ceraulian (ID: 17727560/0x010E8048) looks at Arminibit (ID: 17727559/0x010E8047)
  7: 0x0022 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0023 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Ceraulian (ID: 17727560/0x010E8048) Render.Flags0 and Render.Flags3 conditions are met
  9: 0x0028 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [Ceraulian (ID: 17727560/0x010E8048), Ceraulian (ID: 17727560/0x010E8048)], work=20*
 10: 0x0037 [0x2B] Ceraulian (ID: 17727560/0x010E8048) [8333*]:
    → "I heard that to become a dragoon, you had to make a pact with a living wyvern. However, thanks to the dragonslayers, there aren't that many dragons left."
 11: 0x003E [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x003F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
 13: 0x004E [0x2B] Arminibit (ID: 17727559/0x010E8047) [8334*]:
    → "The dragonslayers keep down the number of deadly dragons, but the number of dragoons can never go up. It's a sad, sad cycle."
 14: 0x0055 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0056 [0x2B] Arminibit (ID: 17727559/0x010E8047) [8335*]:
    → "They say that King Ranperre's top vassal, the "Last of the Dragoons," collapsed after a battle with a dragonslayer."
 16: 0x005D [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x005E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 18: 0x0063 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [Ceraulian (ID: 17727560/0x010E8048), Ceraulian (ID: 17727560/0x010E8048)], work=20*
 19: 0x0072 [0x2B] Ceraulian (ID: 17727560/0x010E8048) [8336*]:
    → "I even heard a rumor that a new dragoon appeared in San d'Oria, but no one has ever seen him. Some even say that it is that Cyranuce, locked up in the dungeons."
 20: 0x0079 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x007A [0x2B] Arminibit (ID: 17727559/0x010E8047) [8337*]:
    → "There's nothing to those rumors. If he really was a dragoon, why would he be in the Oubliette?"
 22: 0x0081 [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x0082 [0x2B] Ceraulian (ID: 17727560/0x010E8048) [8338*]:
    → "You have a point..."
 24: 0x0089 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x008A [0x21] END_EVENT
 26: 0x008B [0x00] END_REQSTACK()
```

### Event 18

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x008C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                      00                       .   
```

#### Opcodes

```
  0: 0x008C [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008D   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         1E F0 FF               ...
0090: FF 7F 2B 47 80 0E 01 08  80 23 21 00              ..+G.....#!.    
```

#### Opcodes

```
  0: 0x008D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0092 [0x2B] Arminibit (ID: 17727559/0x010E8047) [8360*]:
    → "Meeting your quota is an iron rule of the Brugaire Consortium. I've seen more than a few prospective merchants shown the door after failing to observe it. The business world is an unforgiving place."
  2: 0x0099 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x009A [0x21] END_EVENT
  4: 0x009B [0x00] END_REQSTACK()
```

### Event 17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                      00                       .   
```

#### Opcodes

```
  0: 0x009C [0x00] END_REQSTACK()
```

### Event 0

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009D   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                         1E F0 FF               ...
00A0: FF 7F 2B 47 80 0E 01 09  80 23 21 00              ..+G.....#!.    
```

#### Opcodes

```
  0: 0x009D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00A2 [0x2B] Arminibit (ID: 17727559/0x010E8047) [8376*]:
    → "The boss has never talked about his family before... It's kinda surprising that he even has a father in the first place."
  2: 0x00A9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00AA [0x21] END_EVENT
  4: 0x00AB [0x00] END_REQSTACK()
```

### Event 1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AC   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                      1E F0 FF FF              ....
00B0: 7F 2B 47 80 0E 01 0A 80  23 21 00                 .+G.....#!.     
```

#### Opcodes

```
  0: 0x00AC [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00B1 [0x2B] Arminibit (ID: 17727559/0x010E8047) [8427*]:
    → "I might send my mother something nice for the holidays. We've all but disowned each other, so it makes it difficult for me to just drop in."
  2: 0x00B8 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00B9 [0x21] END_EVENT
  4: 0x00BA [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BB   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                   1E F0 FF FF 7F             .....
00C0: 2B 47 80 0E 01 0B 80 23  21 00                    +G.....#!.      
```

#### Opcodes

```
  0: 0x00BB [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00C0 [0x2B] Arminibit (ID: 17727559/0x010E8047) [8442*]:
    → "Urgh... I think I'm gonna struggle to get clear this week. But you'll be there to bail me out, right!?"
  2: 0x00C7 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00C8 [0x21] END_EVENT
  4: 0x00C9 [0x00] END_REQSTACK()
```

### Event 7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00CA  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                00                           .     
```

#### Opcodes

```
  0: 0x00CA [0x00] END_REQSTACK()
```

### Event 19

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00CB  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                   00                         .    
```

#### Opcodes

```
  0: 0x00CB [0x00] END_REQSTACK()
```

### Event 15

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00CC  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                      00                       .   
```

#### Opcodes

```
  0: 0x00CC [0x00] END_REQSTACK()
```

### Event 22

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00CD  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                         00                     .  
```

#### Opcodes

```
  0: 0x00CD [0x00] END_REQSTACK()
```

### Event 586

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CE   |
| Data Size    | 63 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                            66 01                f.
00D0: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 1D 0C 80  .........tlk0...
00E0: 23 5E 69 64 6C 30 1C 0D  80 1E F0 FF FF 7F 6F 70  #^idl0........op
00F0: 66 01 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 1D  f..........tlk0.
0100: 0E 80 23 5E 69 64 6C 30  1C 0F 80 21 00           ..#^idl0...!.   
```

#### Opcodes

```
  0: 0x00CE [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  1: 0x00DD [0x1D] PRINT_EVENT_MESSAGE(message_id=7884*)
    → "I've told Fontoumant, so all you have to do is deliver the goods to Avandale as..."
  2: 0x00E0 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00E1 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  4: 0x00E6 [0x1C] WAIT(60* ticks)
  5: 0x00E9 [0x1E] EventEntity looks at LocalPlayer and starts talking
  6: 0x00EE [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x00EF [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  8: 0x00F0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  9: 0x00FF [0x1D] PRINT_EVENT_MESSAGE(message_id=7885*)
    → "Hey! There're some things best left unheard, stranger. I trust you'll be leaving... Now!"
 10: 0x0102 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0103 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 12: 0x0108 [0x1C] WAIT(30* ticks)
 13: 0x010B [0x21] END_EVENT
 14: 0x010C [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                         37 10 80               7..
0110: 11 80 12 80 13 80 00                              .......         
```

#### Opcodes

```
  0: 0x010D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-0.888*, z=-113.694*, y=-4.000*, direction=292.1°*
  1: 0x0116 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0117   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                      32  14 80 1F 00 15 80 16 80         2........
0120: 12 80 1F 01 6F 1E 49 80  0E 01 00                 ....o.I....     
```

#### Opcodes

```
  0: 0x0117 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x011A [0x1F] MOVE_ENTITY: EventEntity moves to X=0.627*, Z=-109.145*, Y=-4.000*
  2: 0x0122 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0124 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0125 [0x1E] EventEntity looks at Brugaire (ID: 17727561/0x010E8049) and starts talking
  5: 0x012A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012B   |
| Data Size    | 22 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                   32 14 80 1F 00             2....
0130: 17 80 18 80 19 80 1F 01  6F 1E 49 80 0E 01 6F 70  ........o.I...op
0140: 00                                                .               
```

#### Opcodes

```
  0: 0x012B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x012E [0x1F] MOVE_ENTITY: EventEntity moves to X=2.029*, Z=-121.012*, Y=-8.000*
  2: 0x0136 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0138 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0139 [0x1E] EventEntity looks at Brugaire (ID: 17727561/0x010E8049) and starts talking
  5: 0x013E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x013F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x0140 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0141   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:    66 01 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0150: 1C 0D 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0141 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  1: 0x0150 [0x1C] WAIT(60* ticks)
  2: 0x0153 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0154  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:             5E 69 64 6C  30 1C 0D 80 00               ^idl0....   
```

#### Opcodes

```
  0: 0x0154 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0159 [0x1C] WAIT(60* ticks)
  2: 0x015C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015D   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                         66 01 80               f..
0160: F8 FF FF 7F F8 FF FF 7F  74 68 6B 31 1C 0D 80 00  ........thk1....
```

#### Opcodes

```
  0: 0x015D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=20*
  1: 0x016C [0x1C] WAIT(60* ticks)
  2: 0x016F [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0170   |
| Data Size    | 32 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170: 53 F8 FF FF 7F F8 FF FF  7F 74 68 6B 31 66 01 80  S........thk1f..
0180: F8 FF FF 7F F8 FF FF 7F  74 68 6B 32 1C 0D 80 00  ........thk2....
```

#### Opcodes

```
  0: 0x0170 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x017D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=20*
  2: 0x018C [0x1C] WAIT(60* ticks)
  3: 0x018F [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0190   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190: 66 01 80 F8 FF FF 7F F8  FF FF 7F 70 61 73 30 53  f..........pas0S
01A0: F8 FF FF 7F F8 FF FF 7F  70 61 73 30 00           ........pas0.   
```

#### Opcodes

```
  0: 0x0190 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=20*
  1: 0x019F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  2: 0x01AC [0x00] END_REQSTACK()
```
