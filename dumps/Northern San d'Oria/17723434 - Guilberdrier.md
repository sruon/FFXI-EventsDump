# 17723434 - Guilberdrier

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 456 bytes                     |
| Total Events     | 8                             |
| References Count | 17                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [521](#event-521)        | 0x0001       |      1 |              1 |
| [522](#event-522)        | 0x0002       |    129 |             29 |
| [518](#event-518)        | 0x0083       |     89 |             17 |
| [65535.1](#event-655351) | 0x00DC       |     32 |              8 |
| [65535.2](#event-655352) | 0x00FC       |     32 |              8 |
| [16](#event-16)          | 0x011C       |     28 |              5 |
| [0](#event-0)            | 0x0138       |     28 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x2BA2      |       11170 |
|       2 | 0x001E      |          30 |
|       3 | 0x2BA4      |       11172 |
|       4 | 0x2BA6      |       11174 |
|       5 | 0x2BAB      |       11179 |
|       6 | 0x2BAC      |       11180 |
|       7 | 0x00C9      |         201 |
|       8 | 0x0000      |           0 |
|       9 | 0x13808     |       79880 |
|      10 | 0x14C73     |       85107 |
|      11 | 0x06D5      |        1749 |
|      12 | 0x0F54      |        3924 |
|      13 | 0xFFFFD486  |  4294956166 |
|      14 | 0x16F21     |       93985 |
|      15 | 0xFFFFFF39  |  4294967097 |
|      16 | 0x0F28      |        3880 |

## String References

- **11170**: What do you want?
- **11172**: Speaking of money, I haven't seen that gambler all day. Has he run off again?
- **11174**: Who does he think he is, running off when we've piles of work to do! I'll give him a good lashing when he gets back!
- **11179**: Hey, it's that recruit from before. So you're the one who got Varchet to show up again!
- **11180**: I don't remember asking you to fetch him, but I owe you my thanks anyway. Here, take this!

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

### Event 521

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

### Event 522

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0002    |
| Data Size    | 129 bytes |
| Instructions | 29        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1E F0 FF FF 7F 6F  70 66 00 80 F8 FF FF 7F    .....opf......
0010: F8 FF FF 7F 74 6C 6B 30  1D 01 80 23 5E 69 64 6C  ....tlk0...#^idl
0020: 30 1C 02 80 27 5F 29 70  0E 01 05 2A 5F 29 70 0E  0...'_)p...*_)p.
0030: 01 1C 02 80 1E 29 70 0E  01 6F 70 66 00 80 F8 FF  .....)p..opf....
0040: FF 7F F8 FF FF 7F 74 6C  6B 30 1D 03 80 23 5E 69  ......tlk0...#^i
0050: 64 6C 30 1C 02 80 27 60  29 70 0E 01 06 2A 60 29  dl0...'`)p...*`)
0060: 70 0E 01 1C 02 80 66 00  80 F8 FF FF 7F F8 FF FF  p.....f.........
0070: 7F 74 6C 6B 30 1D 04 80  23 5E 69 64 6C 30 1C 02  .tlk0...#^idl0..
0080: 80 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0007 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0008 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=11170*)
    → "What do you want?"
  5: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001C [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x0021 [0x1C] WAIT(30* ticks)
  8: 0x0024 [0x27] REQ_SET(priority=0x5F, entity_id=Aurege (ID: 17723433/0x010E7029), tag_num=0x05)
  9: 0x002B [0x2A] GET_REQ_LEVEL(level=95, entity_id=Aurege (ID: 17723433/0x010E7029))
 10: 0x0031 [0x1C] WAIT(30* ticks)
 11: 0x0034 [0x1E] EventEntity looks at Aurege (ID: 17723433/0x010E7029) and starts talking
 12: 0x0039 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 13: 0x003A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 14: 0x003B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
 15: 0x004A [0x1D] PRINT_EVENT_MESSAGE(message_id=11172*)
    → "Speaking of money, I haven't seen that gambler all day. Has he run off again?"
 16: 0x004D [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x004E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 18: 0x0053 [0x1C] WAIT(30* ticks)
 19: 0x0056 [0x27] REQ_SET(priority=0x60, entity_id=Aurege (ID: 17723433/0x010E7029), tag_num=0x06)
 20: 0x005D [0x2A] GET_REQ_LEVEL(level=96, entity_id=Aurege (ID: 17723433/0x010E7029))
 21: 0x0063 [0x1C] WAIT(30* ticks)
 22: 0x0066 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
 23: 0x0075 [0x1D] PRINT_EVENT_MESSAGE(message_id=11174*)
    → "Who does he think he is, running off when we've piles of work to do! I'll give him a good lashing when he gets back!"
 24: 0x0078 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x0079 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 26: 0x007E [0x1C] WAIT(30* ticks)
 27: 0x0081 [0x21] END_EVENT
 28: 0x0082 [0x00] END_REQSTACK()
```

### Event 518

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0083   |
| Data Size    | 89 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:          42 1E F0 FF FF  7F 6F 70 66 00 80 F8 FF     B.....opf....
0090: FF 7F F8 FF FF 7F 74 6C  6B 30 1D 05 80 23 5E 69  ......tlk0...#^i
00A0: 64 6C 30 1C 02 80 66 00  80 F8 FF FF 7F F8 FF FF  dl0...f.........
00B0: 7F 70 61 73 30 1D 06 80  23 53 F8 FF FF 7F F8 FF  .pas0...#S......
00C0: FF 7F 70 61 73 30 45 07  80 F0 FF FF 7F F0 FF FF  ..pas0E.........
00D0: 7F 71 73 74 63 08 80 1C  02 80 21 00              .qstc.....!.    
```

#### Opcodes

```
  0: 0x0083 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0084 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0089 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x008A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x008B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  5: 0x009A [0x1D] PRINT_EVENT_MESSAGE(message_id=11179*)
    → "Hey, it's that recruit from before. So you're the one who got Varchet to show up again!"
  6: 0x009D [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x009E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  8: 0x00A3 [0x1C] WAIT(30* ticks)
  9: 0x00A6 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=20*
 10: 0x00B5 [0x1D] PRINT_EVENT_MESSAGE(message_id=11180*)
    → "I don't remember asking you to fetch him, but I owe you my thanks anyway. Here, take this!"
 11: 0x00B8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x00B9 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
 13: 0x00C6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 14: 0x00D7 [0x1C] WAIT(30* ticks)
 15: 0x00DA [0x21] END_EVENT
 16: 0x00DB [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DC   |
| Data Size    | 32 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                      1E 29 70 0E              .)p.
00E0: 01 6F 70 66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  .opf..........tl
00F0: 6B 30 1D 03 80 23 5E 69  64 6C 30 00              k0...#^idl0.    
```

#### Opcodes

```
  0: 0x00DC [0x1E] EventEntity looks at Aurege (ID: 17723433/0x010E7029) and starts talking
  1: 0x00E1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00E2 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00E3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x00F2 [0x1D] PRINT_EVENT_MESSAGE(message_id=11172*)
    → "Speaking of money, I haven't seen that gambler all day. Has he run off again?"
  5: 0x00F5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00F6 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x00FB [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FC   |
| Data Size    | 32 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                      1E F0 FF FF              ....
0100: 7F 6F 70 66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  .opf..........tl
0110: 6B 30 1D 04 80 23 5E 69  64 6C 30 00              k0...#^idl0.    
```

#### Opcodes

```
  0: 0x00FC [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0101 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0102 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0103 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0112 [0x1D] PRINT_EVENT_MESSAGE(message_id=11174*)
    → "Who does he think he is, running off when we've piles of work to do! I'll give him a good lashing when he gets back!"
  5: 0x0115 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0116 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x011B [0x00] END_REQSTACK()
```

### Event 16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011C   |
| Data Size    | 28 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                      22 00 92 01              "...
0120: F8 FF FF 7F 37 09 80 0A  80 0B 80 0C 80 79 00 F8  ....7........y..
0130: FF FF 7F 04 70 0E 01 00                           ....p...        
```

#### Opcodes

```
  0: 0x011C [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x011E [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0124 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=79.880*, z=85.107*, y=1.749*, direction=344.9°*
  3: 0x012D [0x79] EventEntity looks at Claidie (ID: 17723396/0x010E7004) (Basic look)
  4: 0x0137 [0x00] END_REQSTACK()
```

### Event 0

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0138   |
| Data Size    | 28 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                          22 00 92 01 F8 FF FF 7F          ".......
0140: 37 0D 80 0E 80 0F 80 10  80 79 00 F8 FF FF 7F 02  7........y......
0150: 70 0E 01 00                                       p...            
```

#### Opcodes

```
  0: 0x0138 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x013A [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0140 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-11.130*, z=93.985*, y=-0.199*, direction=341.0°*
  3: 0x0149 [0x79] EventEntity looks at Trion (ID: 17723394/0x010E7002) (Basic look)
  4: 0x0153 [0x00] END_REQSTACK()
```
