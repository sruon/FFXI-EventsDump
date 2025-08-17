# 17727498 - Thierride

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Port San d'Oria (ID: 232) |
| Block Size       | 944 bytes                 |
| Total Events     | 18                        |
| References Count | 34                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [500](#event-500)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |      1 |              1 |
| [65535.2](#event-655352) | 0x0003       |     23 |              5 |
| [524](#event-524)        | 0x001A       |     36 |             10 |
| [527](#event-527)        | 0x003E       |      1 |              1 |
| [65535.3](#event-655353) | 0x003F       |      6 |              2 |
| [521](#event-521)        | 0x0045       |    381 |             62 |
| [526](#event-526)        | 0x01C2       |     42 |              8 |
| [528](#event-528)        | 0x01EC       |     63 |             15 |
| [529](#event-529)        | 0x022B       |     36 |             10 |
| [534](#event-534)        | 0x024F       |     36 |             10 |
| [539](#event-539)        | 0x0273       |     69 |             25 |
| [792](#event-792)        | 0x02B8       |      1 |              1 |
| [793](#event-793)        | 0x02B9       |      1 |              1 |
| [794](#event-794)        | 0x02BA       |      1 |              1 |
| [65535.4](#event-655354) | 0x02BB       |     10 |              2 |
| [65535.5](#event-655355) | 0x02C5       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFF98D5  |  4294940885 |
|       1 | 0xFFFEE52F  |  4294894895 |
|       2 | 0xFFFFF061  |  4294963297 |
|       3 | 0x0FFF      |        4095 |
|       4 | 0x000D      |          13 |
|       5 | 0x4C68      |       19560 |
|       6 | 0xFFFEEA0A  |  4294896138 |
|       7 | 0x001E      |          30 |
|       8 | 0x1CFB      |        7419 |
|       9 | 0x016D      |         365 |
|      10 | 0x0084      |         132 |
|      11 | 0x0000      |           0 |
|      12 | 0x00C8      |         200 |
|      13 | 0x0003      |           3 |
|      14 | 0x1CFC      |        7420 |
|      15 | 0x0014      |          20 |
|      16 | 0x1CFD      |        7421 |
|      17 | 0x1CFE      |        7422 |
|      18 | 0x1CFF      |        7423 |
|      19 | 0x1D00      |        7424 |
|      20 | 0x1106      |        4358 |
|      21 | 0x1D11      |        7441 |
|      22 | 0x1113      |        4371 |
|      23 | 0x1D16      |        7446 |
|      24 | 0x00C9      |         201 |
|      25 | 0x1D13      |        7443 |
|      26 | 0x1D1E      |        7454 |
|      27 | 0x1D89      |        7561 |
|      28 | 0x1D8A      |        7562 |
|      29 | 0x1D8B      |        7563 |
|      30 | 0x1D8C      |        7564 |
|      31 | 0x1D8D      |        7565 |
|      32 | 0x0001      |           1 |
|      33 | 0x0080      |         128 |

## String References

- **7419**: Welcome. What'll it be?
- **7441**: Hmm... If only I had five $0, I could make something for him.
- **7443**: What? I didn't ask for this.
- **7446**: Altana bless you! I can finally make my customers some $0! Give me that meat, then, and I'll make sure you're paid.
- **7454**: What? Something wrong with my food?
- **7561**: What's this? A parcel, for me?
- **7562**: But you're an adventurer, are you not?
- **7563**: There's got to be plenty of work for your type! Don't waste your time hauling parcels to and fro.
- **7564**: This kingdom honors those who carry swords, not parcels, in case you hadn't noticed.
- **7565**: Leave the package delivery to those with nothing better to do!

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

### Event 500

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

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          37 00 80 01 80  02 80 03 80 32 04 80 1F     7........2...
0010: 00 05 80 06 80 02 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x0003 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-26.411*, z=-72.401*, y=-3.999*, direction=359.9°*
  1: 0x000C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=19.560*, Z=-71.158*, Y=-3.999*
  3: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0019 [0x00] END_REQSTACK()
```

### Event 524

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 36 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                1E F0 FF FF 7F 6F            .....o
0020: 70 5B 07 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  p[..........tlk0
0030: 1D 08 80 23 5E 69 64 6C  30 1C 07 80 21 00        ...#^idl0...!.  
```

#### Opcodes

```
  0: 0x001A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0020 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0021 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  4: 0x0030 [0x1D] PRINT_EVENT_MESSAGE(message_id=7419*)
    → "Welcome. What'll it be?"
  5: 0x0033 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0034 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x0039 [0x1C] WAIT(30* ticks)
  8: 0x003C [0x21] END_EVENT
  9: 0x003D [0x00] END_REQSTACK()
```

### Event 527

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            00                   . 
```

#### Opcodes

```
  0: 0x003E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003F  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               5E                 ^
0040: 69 64 6C 30 00                                    idl0.           
```

#### Opcodes

```
  0: 0x003F [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0044 [0x00] END_REQSTACK()
```

### Event 521

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0045    |
| Data Size    | 381 bytes |
| Instructions | 62        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                46 01 42  75 00 09 80 75 01 27 64       F.Bu...u.'d
0050: F0 FF FF 7F 24 2A 64 F0  FF FF 7F 45 0A 80 F0 FF  ....$*d....E....
0060: FF 7F F0 FF FF 7F 73 30  35 37 0B 80 45 0C 80 F0  ......s057..E...
0070: FF FF 7F F0 FF FF 7F 66  64 69 31 0B 80 38 0D 80  .......fdi1..8..
0080: 1E F0 FF FF 7F 6F 70 5B  07 80 0A 80 0E 01 0A 80  .....op[........
0090: 0E 01 74 6C 6B 30 1D 08  80 23 5E 69 64 6C 30 1C  ..tlk0...#^idl0.
00A0: 07 80 45 0A 80 F0 FF FF  7F F0 FF FF 7F 73 30 36  ..E..........s06
00B0: 31 0B 80 4A 0B 80 0E 01  0C 80 0E 01 6F 76 0B 80  1..J........ov..
00C0: 0E 01 5B 07 80 0B 80 0E  01 0B 80 0E 01 74 6C 6B  ..[..........tlk
00D0: 30 2B 0B 80 0E 01 0E 80  23 1C 07 80 27 65 0B 80  0+......#...'e..
00E0: 0E 01 01 2A 65 0B 80 0E  01 1C 07 80 27 64 F0 FF  ...*e.......'d..
00F0: FF 7F 21 45 0A 80 F0 FF  FF 7F F0 FF FF 7F 73 30  ..!E..........s0
0100: 35 39 0B 80 4A 0C 80 0E  01 0B 80 0E 01 6F 76 0C  59..J........ov.
0110: 80 0E 01 66 0F 80 0C 80  0E 01 0C 80 0E 01 74 6C  ...f..........tl
0120: 6B 30 2B 0C 80 0E 01 10  80 23 1C 07 80 27 66 0C  k0+......#...'f.
0130: 80 0E 01 01 2A 66 0C 80  0E 01 1C 07 80 45 0A 80  ....*f.......E..
0140: F0 FF FF 7F F0 FF FF 7F  73 30 36 30 0B 80 5B 07  ........s060..[.
0150: 80 0B 80 0E 01 0B 80 0E  01 74 6C 6B 30 2B 0B 80  .........tlk0+..
0160: 0E 01 11 80 23 1C 07 80  27 65 0B 80 0E 01 01 2A  ....#...'e.....*
0170: 65 0B 80 0E 01 1C 07 80  45 0A 80 F0 FF FF 7F F0  e.......E.......
0180: FF FF 7F 73 30 36 31 0B  80 66 0F 80 0C 80 0E 01  ...s061..f......
0190: 0C 80 0E 01 74 6C 6B 30  2B 0C 80 0E 01 12 80 23  ....tlk0+......#
01A0: 1C 07 80 2B 0C 80 0E 01  13 80 23 1C 07 80 27 66  ...+......#...'f
01B0: 0C 80 0E 01 01 2A 66 0C  80 0E 01 1C 07 80 46 00  .....*f.......F.
01C0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0045 [0x46] CAMERA_CONTROL: Disable user control
  1: 0x0047 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0048 [0x75] LOAD_ROOM(Load indoor room, room=365*)
  3: 0x004C [0x75] LOAD_ROOM(No action)
  4: 0x004E [0x27] REQ_SET(priority=0x64, entity_id=LocalPlayer, tag_num=0x24)
  5: 0x0055 [0x2A] GET_REQ_LEVEL(level=100, entity_id=LocalPlayer)
  6: 0x005B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s057" with entities [LocalPlayer, LocalPlayer], work=[132*, 0*]
  7: 0x006C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x007D [0x38] SET_CLIENT_EVENT_MODE(mode=3*)
  9: 0x0080 [0x1E] EventEntity looks at LocalPlayer and starts talking
 10: 0x0085 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 11: 0x0086 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 12: 0x0087 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Thierride (ID: 17727498/0x010E800A), Thierride (ID: 17727498/0x010E800A)], work=30*
 13: 0x0096 [0x1D] PRINT_EVENT_MESSAGE(message_id=7419*)
    → "Welcome. What'll it be?"
 14: 0x0099 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x009A [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 16: 0x009F [0x1C] WAIT(30* ticks)
 17: 0x00A2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s061" with entities [LocalPlayer, LocalPlayer], work=[132*, 0*]
 18: 0x00B3 [0x4A] Gulemont (ID: 17727499/0x010E800B) looks at Ilgusin (ID: 17727500/0x010E800C)
 19: 0x00BC [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 20: 0x00BD [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Gulemont (ID: 17727499/0x010E800B) Render.Flags0 and Render.Flags3 conditions are met
 21: 0x00C2 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Gulemont (ID: 17727499/0x010E800B), Gulemont (ID: 17727499/0x010E800B)], work=30*
 22: 0x00D1 [0x2B] Gulemont (ID: 17727499/0x010E800B) [7420*]:
    → "I clearly heard that the knights were planning a strike on those Ghelsba Orcs. Whatever came of that?"
 23: 0x00D8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x00D9 [0x1C] WAIT(30* ticks)
 25: 0x00DC [0x27] REQ_SET(priority=0x65, entity_id=Gulemont (ID: 17727499/0x010E800B), tag_num=0x01)
 26: 0x00E3 [0x2A] GET_REQ_LEVEL(level=101, entity_id=Gulemont (ID: 17727499/0x010E800B))
 27: 0x00E9 [0x1C] WAIT(30* ticks)
 28: 0x00EC [0x27] REQ_SET(priority=0x64, entity_id=LocalPlayer, tag_num=0x21)
 29: 0x00F3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s059" with entities [LocalPlayer, LocalPlayer], work=[132*, 0*]
 30: 0x0104 [0x4A] Ilgusin (ID: 17727500/0x010E800C) looks at Gulemont (ID: 17727499/0x010E800B)
 31: 0x010D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 32: 0x010E [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Ilgusin (ID: 17727500/0x010E800C) Render.Flags0 and Render.Flags3 conditions are met
 33: 0x0113 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Ilgusin (ID: 17727500/0x010E800C), Ilgusin (ID: 17727500/0x010E800C)], work=20*
 34: 0x0122 [0x2B] Ilgusin (ID: 17727500/0x010E800C) [7421*]:
    → "Well, how could the two princes possibly organize a raid? They can't even agree on the color of the sky!"
 35: 0x0129 [0x23] WAIT_FOR_DIALOG_INTERACTION
 36: 0x012A [0x1C] WAIT(30* ticks)
 37: 0x012D [0x27] REQ_SET(priority=0x66, entity_id=Ilgusin (ID: 17727500/0x010E800C), tag_num=0x01)
 38: 0x0134 [0x2A] GET_REQ_LEVEL(level=102, entity_id=Ilgusin (ID: 17727500/0x010E800C))
 39: 0x013A [0x1C] WAIT(30* ticks)
 40: 0x013D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s060" with entities [LocalPlayer, LocalPlayer], work=[132*, 0*]
 41: 0x014E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Gulemont (ID: 17727499/0x010E800B), Gulemont (ID: 17727499/0x010E800B)], work=30*
 42: 0x015D [0x2B] Gulemont (ID: 17727499/0x010E800B) [7422*]:
    → "Then, is it true that the first prince to quell the Orcs of Ghelsba will inherit the Kingdom?"
 43: 0x0164 [0x23] WAIT_FOR_DIALOG_INTERACTION
 44: 0x0165 [0x1C] WAIT(30* ticks)
 45: 0x0168 [0x27] REQ_SET(priority=0x65, entity_id=Gulemont (ID: 17727499/0x010E800B), tag_num=0x01)
 46: 0x016F [0x2A] GET_REQ_LEVEL(level=101, entity_id=Gulemont (ID: 17727499/0x010E800B))
 47: 0x0175 [0x1C] WAIT(30* ticks)
 48: 0x0178 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s061" with entities [LocalPlayer, LocalPlayer], work=[132*, 0*]
 49: 0x0189 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Ilgusin (ID: 17727500/0x010E800C), Ilgusin (ID: 17727500/0x010E800C)], work=20*
 50: 0x0198 [0x2B] Ilgusin (ID: 17727500/0x010E800C) [7423*]:
    → "Bah. Simply taking Ghelsba won't make anybody king."
 51: 0x019F [0x23] WAIT_FOR_DIALOG_INTERACTION
 52: 0x01A0 [0x1C] WAIT(30* ticks)
 53: 0x01A3 [0x2B] Ilgusin (ID: 17727500/0x010E800C) [7424*]:
    → "Aye, but he'd be a step closer to the throne! Still, it must be in their blood to quarrel."
 54: 0x01AA [0x23] WAIT_FOR_DIALOG_INTERACTION
 55: 0x01AB [0x1C] WAIT(30* ticks)
 56: 0x01AE [0x27] REQ_SET(priority=0x66, entity_id=Ilgusin (ID: 17727500/0x010E800C), tag_num=0x01)
 57: 0x01B5 [0x2A] GET_REQ_LEVEL(level=102, entity_id=Ilgusin (ID: 17727500/0x010E800C))
 58: 0x01BB [0x1C] WAIT(30* ticks)
 59: 0x01BE [0x46] CAMERA_CONTROL: Restore default settings
 60: 0x01C0 [0x21] END_EVENT
 61: 0x01C1 [0x00] END_REQSTACK()
```

### Event 526

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01C2   |
| Data Size    | 42 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:       03 02 10 14 80 5B  07 80 0A 80 0E 01 0A 80    .....[........
01D0: 0E 01 74 68 6B 30 1D 15  80 23 53 0A 80 0E 01 0A  ..thk0...#S.....
01E0: 80 0E 01 74 68 6B 30 1C  07 80 21 00              ...thk0...!.    
```

#### Opcodes

```
  0: 0x01C2 [0x03] Work_Zone[2] = 4358*
  1: 0x01C7 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk0" with entities [Thierride (ID: 17727498/0x010E800A), Thierride (ID: 17727498/0x010E800A)], work=30*
  2: 0x01D6 [0x1D] PRINT_EVENT_MESSAGE(message_id=7441*)
    → "Hmm... If only I had five $0, I could make something for him."
  3: 0x01D9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x01DA [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk0" with entities [Thierride (ID: 17727498/0x010E800A), Thierride (ID: 17727498/0x010E800A)]
  5: 0x01E7 [0x1C] WAIT(30* ticks)
  6: 0x01EA [0x21] END_EVENT
  7: 0x01EB [0x00] END_REQSTACK()
```

### Event 528

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01EC   |
| Data Size    | 63 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:                                      42 20 01 1E              B ..
01F0: F0 FF FF 7F 6F 70 5B 07  80 0A 80 0E 01 0A 80 0E  ....op[.........
0200: 01 74 6C 6B 30 03 02 10  16 80 1D 17 80 23 5E 69  .tlk0........#^i
0210: 64 6C 30 45 18 80 F0 FF  FF 7F F0 FF FF 7F 71 73  dl0E..........qs
0220: 74 63 0B 80 1C 07 80 20  00 21 00                 tc..... .!.     
```

#### Opcodes

```
  0: 0x01EC [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x01ED [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x01EF [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x01F4 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x01F5 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x01F6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Thierride (ID: 17727498/0x010E800A), Thierride (ID: 17727498/0x010E800A)], work=30*
  6: 0x0205 [0x03] Work_Zone[2] = 4371*
  7: 0x020A [0x1D] PRINT_EVENT_MESSAGE(message_id=7446*)
    → "Altana bless you! I can finally make my customers some $0! Give me that meat, then, and I'll make sure you're paid."
  8: 0x020D [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x020E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 10: 0x0213 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 11: 0x0224 [0x1C] WAIT(30* ticks)
 12: 0x0227 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 13: 0x0229 [0x21] END_EVENT
 14: 0x022A [0x00] END_REQSTACK()
```

### Event 529

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x022B   |
| Data Size    | 36 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:                                   1E F0 FF FF 7F             .....
0230: 6F 70 5B 07 80 0A 80 0E  01 0A 80 0E 01 74 6C 6B  op[..........tlk
0240: 30 1D 19 80 23 5E 69 64  6C 30 1C 07 80 21 00     0...#^idl0...!. 
```

#### Opcodes

```
  0: 0x022B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0230 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0231 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0232 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Thierride (ID: 17727498/0x010E800A), Thierride (ID: 17727498/0x010E800A)], work=30*
  4: 0x0241 [0x1D] PRINT_EVENT_MESSAGE(message_id=7443*)
    → "What? I didn't ask for this."
  5: 0x0244 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0245 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x024A [0x1C] WAIT(30* ticks)
  8: 0x024D [0x21] END_EVENT
  9: 0x024E [0x00] END_REQSTACK()
```

### Event 534

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x024F   |
| Data Size    | 36 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240:                                               1E                 .
0250: F0 FF FF 7F 6F 70 5B 07  80 0A 80 0E 01 0A 80 0E  ....op[.........
0260: 01 74 6C 6B 30 1D 1A 80  23 5E 69 64 6C 30 1C 07  .tlk0...#^idl0..
0270: 80 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x024F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0254 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0255 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0256 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Thierride (ID: 17727498/0x010E800A), Thierride (ID: 17727498/0x010E800A)], work=30*
  4: 0x0265 [0x1D] PRINT_EVENT_MESSAGE(message_id=7454*)
    → "What? Something wrong with my food?"
  5: 0x0268 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0269 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x026E [0x1C] WAIT(30* ticks)
  8: 0x0271 [0x21] END_EVENT
  9: 0x0272 [0x00] END_REQSTACK()
```

### Event 539

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0273   |
| Data Size    | 69 bytes |
| Instructions | 25       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0270:          42 20 01 1E F0  FF FF 7F 6F 70 5B 07 80     B ......op[..
0280: 0A 80 0E 01 0A 80 0E 01  74 6C 6B 30 1D 1B 80 23  ........tlk0...#
0290: 1C 07 80 1D 1C 80 23 1C  07 80 1D 1D 80 23 1C 07  ......#......#..
02A0: 80 1D 1E 80 23 1C 07 80  1D 1F 80 23 5E 69 64 6C  ....#......#^idl
02B0: 30 1C 07 80 20 00 21 00                           0... .!.        
```

#### Opcodes

```
  0: 0x0273 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0274 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x0276 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x027B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x027C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x027D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Thierride (ID: 17727498/0x010E800A), Thierride (ID: 17727498/0x010E800A)], work=30*
  6: 0x028C [0x1D] PRINT_EVENT_MESSAGE(message_id=7561*)
    → "What's this? A parcel, for me?"
  7: 0x028F [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0290 [0x1C] WAIT(30* ticks)
  9: 0x0293 [0x1D] PRINT_EVENT_MESSAGE(message_id=7562*)
    → "But you're an adventurer, are you not?"
 10: 0x0296 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0297 [0x1C] WAIT(30* ticks)
 12: 0x029A [0x1D] PRINT_EVENT_MESSAGE(message_id=7563*)
    → "There's got to be plenty of work for your type! Don't waste your time hauling parcels to and fro."
 13: 0x029D [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x029E [0x1C] WAIT(30* ticks)
 15: 0x02A1 [0x1D] PRINT_EVENT_MESSAGE(message_id=7564*)
    → "This kingdom honors those who carry swords, not parcels, in case you hadn't noticed."
 16: 0x02A4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x02A5 [0x1C] WAIT(30* ticks)
 18: 0x02A8 [0x1D] PRINT_EVENT_MESSAGE(message_id=7565*)
    → "Leave the package delivery to those with nothing better to do!"
 19: 0x02AB [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x02AC [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 21: 0x02B1 [0x1C] WAIT(30* ticks)
 22: 0x02B4 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 23: 0x02B6 [0x21] END_EVENT
 24: 0x02B7 [0x00] END_REQSTACK()
```

### Event 792

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x02B8  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02B0:                          00                               .       
```

#### Opcodes

```
  0: 0x02B8 [0x00] END_REQSTACK()
```

### Event 793

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x02B9  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02B0:                             00                             .      
```

#### Opcodes

```
  0: 0x02B9 [0x00] END_REQSTACK()
```

### Event 794

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x02BA  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02B0:                                00                           .     
```

#### Opcodes

```
  0: 0x02BA [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02BB   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02B0:                                   6C 0A 80 0E 01             l....
02C0: 0B 80 20 80 00                                    .. ..           
```

#### Opcodes

```
  0: 0x02BB [0x6C] FADE_ENTITY_COLOR(entity_id=Thierride (ID: 17727498/0x010E800A), end_alpha=0*, fade_time=1*)
  1: 0x02C4 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02C5   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02C0:                6C 0A 80  0E 01 21 80 20 80 00          l....!. .. 
```

#### Opcodes

```
  0: 0x02C5 [0x6C] FADE_ENTITY_COLOR(entity_id=Thierride (ID: 17727498/0x010E800A), end_alpha=128*, fade_time=1*)
  1: 0x02CE [0x00] END_REQSTACK()
```
