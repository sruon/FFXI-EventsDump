# 17171192 - Robel-Akbel

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Fort Karugo-Narugo [S] (ID: 96) |
| Block Size       | 408 bytes                       |
| Total Events     | 14                              |
| References Count | 35                              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [103](#event-103)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     12 |              3 |
| [65535.2](#event-655352) | 0x000E       |     25 |              3 |
| [65535.3](#event-655353) | 0x0027       |     15 |              5 |
| [106](#event-106)        | 0x0036       |      1 |              1 |
| [65535.4](#event-655354) | 0x0037       |     20 |              6 |
| [65535.5](#event-655355) | 0x004B       |     15 |              5 |
| [65535.6](#event-655356) | 0x005A       |     12 |              3 |
| [65535.7](#event-655357) | 0x0066       |     24 |              6 |
| [65535.8](#event-655358) | 0x007E       |     29 |              7 |
| [111](#event-111)        | 0x009B       |      1 |              1 |
| [65535.9](#event-655359) | 0x009C       |     38 |              4 |
| [113](#event-113)        | 0x00C2       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x27A22     |      162338 |
|       1 | 0x6F09      |       28425 |
|       2 | 0xFFFF55F1  |  4294923761 |
|       3 | 0x03B6      |         950 |
|       4 | 0x0004      |           4 |
|       5 | 0x0000      |           0 |
|       6 | 0x0001      |           1 |
|       7 | 0x0016      |          22 |
|       8 | 0x27254     |      160340 |
|       9 | 0x5549      |       21833 |
|      10 | 0xFFFF577A  |  4294924154 |
|      11 | 0x000D      |          13 |
|      12 | 0xFFFF2EB4  |  4294913716 |
|      13 | 0xFFFFF19C  |  4294963612 |
|      14 | 0xFFFED786  |  4294891398 |
|      15 | 0x0010      |          16 |
|      16 | 0xFFFF2846  |  4294912070 |
|      17 | 0xFFFFFCA8  |  4294966440 |
|      18 | 0xFFFED6FD  |  4294891261 |
|      19 | 0x1E32B     |      123691 |
|      20 | 0x0E9D      |        3741 |
|      21 | 0xFFFF3E04  |  4294917636 |
|      22 | 0x0012      |          18 |
|      23 | 0x0028      |          40 |
|      24 | 0x1F911     |      129297 |
|      25 | 0x0CB7      |        3255 |
|      26 | 0xFFFF3DA0  |  4294917536 |
|      27 | 0x1F689     |      128649 |
|      28 | 0x11C7      |        4551 |
|      29 | 0xFFFF3FFE  |  4294918142 |
|      30 | 0x1EBDF     |      125919 |
|      31 | 0x113B      |        4411 |
|      32 | 0x008C      |         140 |
|      33 | 0x00AD      |         173 |
|      34 | 0x0172      |         370 |

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

### Event 103

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       33 01 37 00 80 01  80 02 80 03 80 00          3.7.........  
```

#### Opcodes

```
  0: 0x0002 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0004 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=162.338*, z=28.425*, y=-43.535*, direction=83.5°*
  2: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            7E 06                ~.
0010: F8 02 06 01 04 80 05 80  06 80 06 80 06 80 06 80  ................
0020: 7E 04 F8 02 06 01 00                              ~......         
```

#### Opcodes

```
  0: 0x000E [0x7E] CHOCOBO_MOUNT: Mode 6 (custom mount) on Robel-Akbel (ID: 17171192/0x010602F8)
  1: 0x0020 [0x7E] CHOCOBO_MOUNT: Mode 4 on Robel-Akbel (ID: 17171192/0x010602F8)
  2: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      32  07 80 1F 00 08 80 09 80         2........
0030: 0A 80 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x0027 [0x32] ExtData[1]->MainSpeed = 22* * 0.1
  1: 0x002A [0x1F] MOVE_ENTITY: EventEntity moves to X=160.340*, Z=21.833*, Y=-43.142*
  2: 0x0032 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0034 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0035 [0x00] END_REQSTACK()
```

### Event 106

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0036  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   00                                    .         
```

#### Opcodes

```
  0: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      32  0B 80 1F 00 0C 80 0D 80         2........
0040: 0E 80 1F 01 6F 1E 21 03  06 01 00                 ....o.!....     
```

#### Opcodes

```
  0: 0x0037 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003A [0x1F] MOVE_ENTITY: EventEntity moves to X=-53.580*, Z=-3.684*, Y=-75.898*
  2: 0x0042 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0044 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0045 [0x1E] EventEntity looks at Kamolo-Domilo (ID: 17171233/0x01060321) and starts talking
  5: 0x004A [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004B   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   32 0F 80 1F 00             2....
0050: 10 80 11 80 12 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x004B [0x32] ExtData[1]->MainSpeed = 16* * 0.1
  1: 0x004E [0x1F] MOVE_ENTITY: EventEntity moves to X=-55.226*, Z=-0.856*, Y=-76.035*
  2: 0x0056 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0058 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0059 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                33 01 37 13 80 14            3.7...
0060: 80 15 80 16 80 00                                 ......          
```

#### Opcodes

```
  0: 0x005A [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x005C [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=123.691*, z=3.741*, y=-49.660*, direction=1.6°*
  2: 0x0065 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0066   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   1E 22  03 06 01 32 17 80 5A 00        ."...2..Z.
0070: 18 80 19 80 1A 80 5A 01  1E 22 03 06 01 00        ......Z.."....  
```

#### Opcodes

```
  0: 0x0066 [0x1E] EventEntity looks at Joseaneaut (ID: 17171234/0x01060322) and starts talking
  1: 0x006B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x006E [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=129.297*, Z=3.255*, Y=-49.760*
  3: 0x0076 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  4: 0x0078 [0x1E] EventEntity looks at Joseaneaut (ID: 17171234/0x01060322) and starts talking
  5: 0x007D [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007E   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                            37 1B                7.
0080: 80 1C 80 1D 80 16 80 32  17 80 1F 00 1E 80 1F 80  .......2........
0090: 1D 80 1F 01 6F 1E F4 02  06 01 00                 ....o......     
```

#### Opcodes

```
  0: 0x007E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=128.649*, z=4.551*, y=-49.154*, direction=1.6°*
  1: 0x0087 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x008A [0x1F] MOVE_ENTITY: EventEntity moves to X=125.919*, Z=4.411*, Y=-49.154*
  3: 0x0092 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0094 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0095 [0x1E] EventEntity looks at Romaa Mihgo (ID: 17171188/0x010602F4) and starts talking
  6: 0x009A [0x00] END_REQSTACK()
```

### Event 111

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   00                         .    
```

#### Opcodes

```
  0: 0x009B [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009C   |
| Data Size    | 38 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                      1C 20 80 BB              . ..
00A0: 21 80 F8 02 06 01 F8 02  06 01 63 73 74 30 05 80  !.........cst0..
00B0: 45 22 80 F0 FF FF 7F F0  FF FF 7F 6B 69 6E 6D 05  E".........kinm.
00C0: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x009C [0x1C] WAIT(140* ticks)
  1: 0x009F [0xBB] LOAD_EVENT_SCHEDULER_ALT: Load scheduler "cst0" with entities [Robel-Akbel (ID: 17171192/0x010602F8), Robel-Akbel (ID: 17171192/0x010602F8)], work=[173*, 0*]
  2: 0x00B0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "kinm" with entities [LocalPlayer, LocalPlayer], work=[370*, 0*]
  3: 0x00C1 [0x00] END_REQSTACK()
```

### Event 113

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C2  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:       00                                            .             
```

#### Opcodes

```
  0: 0x00C2 [0x00] END_REQSTACK()
```
