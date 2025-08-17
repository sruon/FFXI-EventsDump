# 17576401 - Shikaree M

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | The Eldieme Necropolis (ID: 195) |
| Block Size       | 536 bytes                        |
| Total Events     | 25                               |
| References Count | 31                               |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     22 |              4 |
| [65535.3](#event-655353)   | 0x0027       |     16 |              2 |
| [65535.4](#event-655354)   | 0x0037       |     14 |              2 |
| [65535.5](#event-655355)   | 0x0045       |      9 |              3 |
| [4](#event-4)              | 0x004E       |      1 |              1 |
| [65535.6](#event-655356)   | 0x004F       |     10 |              2 |
| [65535.7](#event-655357)   | 0x0059       |     14 |              4 |
| [65535.8](#event-655358)   | 0x0067       |     29 |              4 |
| [65535.9](#event-655359)   | 0x0084       |      5 |              3 |
| [65535.10](#event-6553510) | 0x0089       |      5 |              3 |
| [65535.11](#event-6553511) | 0x008E       |      5 |              3 |
| [65535.12](#event-6553512) | 0x0093       |      5 |              3 |
| [5](#event-5)              | 0x0098       |      1 |              1 |
| [65535.13](#event-6553513) | 0x0099       |     10 |              2 |
| [65535.14](#event-6553514) | 0x00A3       |     14 |              4 |
| [65535.15](#event-6553515) | 0x00B1       |     43 |              7 |
| [65535.16](#event-6553516) | 0x00DC       |     21 |              7 |
| [65535.17](#event-6553517) | 0x00F1       |     30 |              4 |
| [65535.18](#event-6553518) | 0x010F       |      5 |              3 |
| [65535.19](#event-6553519) | 0x0114       |      5 |              3 |
| [65535.20](#event-6553520) | 0x0119       |      5 |              3 |
| [65535.21](#event-6553521) | 0x011E       |      5 |              3 |
| [65535.22](#event-6553522) | 0x0123       |      5 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0167      |         359 |
|       1 | 0x001E      |          30 |
|       2 | 0x0165      |         357 |
|       3 | 0x65F2E     |      417582 |
|       4 | 0xFFFE3177  |  4294848887 |
|       5 | 0xFFFF2541  |  4294911297 |
|       6 | 0x002D      |          45 |
|       7 | 0x000D      |          13 |
|       8 | 0x664B8     |      419000 |
|       9 | 0x1D1E      |        7454 |
|      10 | 0x1D1F      |        7455 |
|      11 | 0x1D20      |        7456 |
|      12 | 0x1D21      |        7457 |
|      13 | 0x28F78     |      167800 |
|      14 | 0xFFFEB703  |  4294883075 |
|      15 | 0xFFFF939B  |  4294939547 |
|      16 | 0x051E      |        1310 |
|      17 | 0x2BC7C     |      179324 |
|      18 | 0xFFFF2090  |  4294910096 |
|      19 | 0xFFFF8301  |  4294935297 |
|      20 | 0xFFFEADE2  |  4294880738 |
|      21 | 0xFFFF94C1  |  4294939841 |
|      22 | 0x0028      |          40 |
|      23 | 0x28488     |      165000 |
|      24 | 0xFFFEA9FA  |  4294879738 |
|      25 | 0x0032      |          50 |
|      26 | 0x1D22      |        7458 |
|      27 | 0x1D29      |        7465 |
|      28 | 0x1D2A      |        7466 |
|      29 | 0x1D2B      |        7467 |
|      30 | 0x1D2C      |        7468 |

## String References

- **7454**: <Player>... You took your time. Perrrhaps you considered giving me the slip?
- **7455**: Even if you tried, it would be a futile effort. You cannot get away from a Mithran Tracker.
- **7456**: Within the Eldieme Necropolis, there is a cemetery divided into four areas where the casualties of the Great War are interred.
- **7457**: There is a stone monument in each rrroom that details who is buried where. First, we should search the stone monuments for the name of the sinner's daughter.
- **7458**: Take the lead. I will follow after you, keeping out of sight.
- **7465**: Well <Player>, let's go and check the grrrave.
- **7466**: ...... She definitely appears to be interred here...
- **7467**: What's this... $1? The daughter's...?
- **7468**: There's nothing left of the body, but... This is enough. There's nothing more we can do here. Let's return to Chieftainness Perih Vashai.

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
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   [..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=359*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 5E 69   S........tlk0^i
0020: 64 6C 30 1C 01 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0023 [0x1C] WAIT(30* ticks)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      5B  02 80 F8 FF FF 7F F8 FF         [........
0030: FF 7F 70 61 73 30 00                              ..pas0.         
```

#### Opcodes

```
  0: 0x0027 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=357*
  1: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0040: 70 61 73 30 00                                    pas0.           
```

#### Opcodes

```
  0: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  1: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0045  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                5E 69 64  6C 30 1C 01 80 00             ^idl0....  
```

#### Opcodes

```
  0: 0x0045 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x004A [0x1C] WAIT(30* ticks)
  2: 0x004D [0x00] END_REQSTACK()
```

### Event 4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            00                   . 
```

#### Opcodes

```
  0: 0x004E [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               37                 7
0050: 03 80 04 80 05 80 06 80  00                       .........       
```

#### Opcodes

```
  0: 0x004F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=417.582*, z=-118.409*, y=-55.999*, direction=4.0°*
  1: 0x0058 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0059   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             32 07 80 1F 00 08 80           2......
0060: 04 80 05 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0059 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005C [0x1F] MOVE_ENTITY: EventEntity moves to X=419.000*, Z=-118.409*, Y=-55.999*
  2: 0x0064 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0066 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0067   |
| Data Size    | 29 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      22  00 2C D1 31 0C 01 D1 31         ".,.1...1
0070: 0C 01 70 6F 70 30 53 F8  FF FF 7F F8 FF FF 7F 70  ..pop0S........p
0080: 6F 70 30 00                                       op0.            
```

#### Opcodes

```
  0: 0x0067 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0069 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "pop0" with entities [Shikaree M (ID: 17576401/0x010C31D1), Shikaree M (ID: 17576401/0x010C31D1)]
  2: 0x0076 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pop0" with entities [EventEntity, EventEntity]
  3: 0x0083 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0084  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             1D 09 80 23  00                           ...#.       
```

#### Opcodes

```
  0: 0x0084 [0x1D] PRINT_EVENT_MESSAGE(message_id=7454*)
    → "<Player>... You took your time. Perrrhaps you considered giving me the slip?"
  1: 0x0087 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0088 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0089  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             1D 0A 80 23 00                 ...#.  
```

#### Opcodes

```
  0: 0x0089 [0x1D] PRINT_EVENT_MESSAGE(message_id=7455*)
    → "Even if you tried, it would be a futile effort. You cannot get away from a Mithran Tracker."
  1: 0x008C [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x008D [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x008E  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                            1D 0B                ..
0090: 80 23 00                                          .#.             
```

#### Opcodes

```
  0: 0x008E [0x1D] PRINT_EVENT_MESSAGE(message_id=7456*)
    → "Within the Eldieme Necropolis, there is a cemetery divided into four areas where the casualties of the Great War are interred."
  1: 0x0091 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0092 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0093  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:          1D 0C 80 23 00                              ...#.        
```

#### Opcodes

```
  0: 0x0093 [0x1D] PRINT_EVENT_MESSAGE(message_id=7457*)
    → "There is a stone monument in each rrroom that details who is buried where. First, we should search the stone monuments for the name of the sinner's daughter."
  1: 0x0096 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0097 [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0098  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                          00                               .       
```

#### Opcodes

```
  0: 0x0098 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0099   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             37 0D 80 0E 80 0F 80           7......
00A0: 10 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0099 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=167.800*, z=-84.221*, y=-27.749*, direction=115.1°*
  1: 0x00A2 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A3   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:          32 07 80 1F 00  11 80 12 80 13 80 1F 01     2............
00B0: 00                                                .               
```

#### Opcodes

```
  0: 0x00A3 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00A6 [0x1F] MOVE_ENTITY: EventEntity moves to X=179.324*, Z=-57.200*, Y=-31.999*
  2: 0x00AE [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00B0 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B1   |
| Data Size    | 43 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:    32 07 80 1F 00 0D 80  14 80 15 80 1F 01 1C 16   2..............
00C0: 80 2C D1 31 0C 01 D1 31  0C 01 72 65 73 30 53 F8  .,.1...1..res0S.
00D0: FF FF 7F F8 FF FF 7F 72  65 73 30 00              .......res0.    
```

#### Opcodes

```
  0: 0x00B1 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00B4 [0x1F] MOVE_ENTITY: EventEntity moves to X=167.800*, Z=-86.558*, Y=-27.455*
  2: 0x00BC [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00BE [0x1C] WAIT(40* ticks)
  4: 0x00C1 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "res0" with entities [Shikaree M (ID: 17576401/0x010C31D1), Shikaree M (ID: 17576401/0x010C31D1)]
  5: 0x00CE [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "res0" with entities [EventEntity, EventEntity]
  6: 0x00DB [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DC   |
| Data Size    | 21 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                      32 07 80 1F              2...
00E0: 00 17 80 18 80 15 80 1F  01 1E F0 FF FF 7F 6F 70  ..............op
00F0: 00                                                .               
```

#### Opcodes

```
  0: 0x00DC [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00DF [0x1F] MOVE_ENTITY: EventEntity moves to X=165.000*, Z=-87.558*, Y=-27.455*
  2: 0x00E7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00E9 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x00EE [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x00EF [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x00F0 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F1   |
| Data Size    | 30 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:    1C 19 80 2C D1 31 0C  01 D1 31 0C 01 72 65 73   ...,.1...1..res
0100: 32 53 F8 FF FF 7F F8 FF  FF 7F 72 65 73 32 00     2S........res2. 
```

#### Opcodes

```
  0: 0x00F1 [0x1C] WAIT(50* ticks)
  1: 0x00F4 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "res2" with entities [Shikaree M (ID: 17576401/0x010C31D1), Shikaree M (ID: 17576401/0x010C31D1)]
  2: 0x0101 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "res2" with entities [EventEntity, EventEntity]
  3: 0x010E [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x010F  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                               1D                 .
0110: 1A 80 23 00                                       ..#.            
```

#### Opcodes

```
  0: 0x010F [0x1D] PRINT_EVENT_MESSAGE(message_id=7458*)
    → "Take the lead. I will follow after you, keeping out of sight."
  1: 0x0112 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0113 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0114  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:             1D 1B 80 23  00                           ...#.       
```

#### Opcodes

```
  0: 0x0114 [0x1D] PRINT_EVENT_MESSAGE(message_id=7465*)
    → "Well <Player>, let's go and check the grrrave."
  1: 0x0117 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0118 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0119  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                             1D 1C 80 23 00                 ...#.  
```

#### Opcodes

```
  0: 0x0119 [0x1D] PRINT_EVENT_MESSAGE(message_id=7466*)
    → "...... She definitely appears to be interred here..."
  1: 0x011C [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x011D [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x011E  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                            1D 1D                ..
0120: 80 23 00                                          .#.             
```

#### Opcodes

```
  0: 0x011E [0x1D] PRINT_EVENT_MESSAGE(message_id=7467*)
    → "What's this... $1? The daughter's...?"
  1: 0x0121 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0122 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0123  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:          1D 1E 80 23 00                              ...#.        
```

#### Opcodes

```
  0: 0x0123 [0x1D] PRINT_EVENT_MESSAGE(message_id=7468*)
    → "There's nothing left of the body, but... This is enough. There's nothing more we can do here. Let's return to Chieftainness Perih Vashai."
  1: 0x0126 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0127 [0x00] END_REQSTACK()
```
