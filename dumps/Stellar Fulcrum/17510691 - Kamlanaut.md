# 17510691 - Kamlanaut

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Stellar Fulcrum (ID: 179) |
| Block Size       | 392 bytes                 |
| Total Events     | 10                        |
| References Count | 19                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      7 |              2 |
| [6](#event-6)            | 0x0007       |     62 |              7 |
| [17](#event-17)          | 0x0045       |     30 |              5 |
| [65535.1](#event-655351) | 0x0063       |     16 |              2 |
| [65535.2](#event-655352) | 0x0073       |     12 |              3 |
| [65535.3](#event-655353) | 0x007F       |     42 |              6 |
| [65535.4](#event-655354) | 0x00A9       |     19 |              3 |
| [65535.5](#event-655355) | 0x00BC       |     14 |              4 |
| [65535.6](#event-655356) | 0x00CA       |     56 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFFFFE2  |  4294967266 |
|       1 | 0xE7FB      |       59387 |
|       2 | 0x1891      |        6289 |
|       3 | 0x0400      |        1024 |
|       4 | 0x0227      |         551 |
|       5 | 0x004E      |          78 |
|       6 | 0x0000      |           0 |
|       7 | 0xA39E      |       41886 |
|       8 | 0x09C3      |        2499 |
|       9 | 0x0380      |         896 |
|      10 | 0x0078      |         120 |
|      11 | 0x0080      |         128 |
|      12 | 0x00B4      |         180 |
|      13 | 0x00BE      |         190 |
|      14 | 0x000D      |          13 |
|      15 | 0xD552      |       54610 |
|      16 | 0x003C      |          60 |
|      17 | 0x00C8      |         200 |
|      18 | 0x0044      |          68 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 94 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0000 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x00] END_REQSTACK()
```

### Event 6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0007   |
| Data Size    | 62 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      22  01 37 00 80 01 80 02 80         ".7......
0010: 03 80 5B 04 80 F0 FF FF  7F F0 FF FF 7F 00 FE FE  ..[.............
0020: FE 62 05 80 F0 FF FF 7F  F0 FF FF 7F 00 FE FE FE  .b..............
0030: 06 80 2C F8 FF FF 7F F8  FF FF 7F 6B 69 6C 6C 5E  ..,........kill^
0040: 62 74 6C 30 00                                    btl0.           
```

#### Opcodes

```
  0: 0x0007 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0009 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-0.030*, z=59.387*, y=6.289*, direction=90.0°*
  2: 0x0012 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler 0xFEFEFE00 with entities [LocalPlayer, LocalPlayer], work=551*
  3: 0x0021 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler 0xFEFEFE00 with entities [LocalPlayer, LocalPlayer], work=[78*, 0*]
  4: 0x0032 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "kill" with entities [EventEntity, EventEntity]
  5: 0x003F [0x5E] EventEntity goes idle (kills current action) (animation: "btl0")
  6: 0x0044 [0x00] END_REQSTACK()
```

### Event 17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 30 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                22 01 37  06 80 07 80 08 80 09 80       ".7........
0050: 2C F8 FF FF 7F F8 FF FF  7F 6B 69 6C 6C 5E 62 74  ,........kill^bt
0060: 6C 30 00                                          l0.             
```

#### Opcodes

```
  0: 0x0045 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0047 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.000*, z=41.886*, y=2.499*, direction=78.7°*
  2: 0x0050 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "kill" with entities [EventEntity, EventEntity]
  3: 0x005D [0x5E] EventEntity goes idle (kills current action) (animation: "btl0")
  4: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0063   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          5B 04 80 F8 FF  FF 7F F8 FF FF 7F 64 77     [..........dw
0070: 6E 31 00                                          n1.             
```

#### Opcodes

```
  0: 0x0063 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dwn1" with entities [EventEntity, EventEntity], work=551*
  1: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          6C 23 31 0B 01  06 80 0A 80 22 01 00        l#1......".. 
```

#### Opcodes

```
  0: 0x0073 [0x6C] FADE_ENTITY_COLOR(entity_id=Kam'lanaut (ID: 17510691/0x010B3123), end_alpha=0*, fade_time=120*)
  1: 0x007C [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  2: 0x007E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007F   |
| Data Size    | 42 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               5B                 [
0080: 04 80 F8 FF FF 7F F8 FF  FF 7F 61 70 70 30 92 01  ..........app0..
0090: F8 FF FF 7F 6C F8 FF FF  7F 06 80 06 80 22 00 6C  ....l........".l
00A0: F8 FF FF 7F 0B 80 0C 80  00                       .........       
```

#### Opcodes

```
  0: 0x007F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "app0" with entities [EventEntity, EventEntity], work=551*
  1: 0x008E [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0094 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=0*)
  3: 0x009D [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  4: 0x009F [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=180*)
  5: 0x00A8 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A9   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                             5B 04 80 F8 FF FF 7F           [......
00B0: F8 FF FF 7F 61 70 70 31  1C 0D 80 00              ....app1....    
```

#### Opcodes

```
  0: 0x00A9 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "app1" with entities [EventEntity, EventEntity], work=551*
  1: 0x00B8 [0x1C] WAIT(190* ticks)
  2: 0x00BB [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BC   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                      32 0E 80 1F              2...
00C0: 00 06 80 0F 80 02 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x00BC [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00BF [0x1F] MOVE_ENTITY: EventEntity moves to X=0.000*, Z=54.610*, Y=6.289*
  2: 0x00C7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00C9 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CA   |
| Data Size    | 56 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                5B 04 80 F8 FF FF            [.....
00D0: 7F F8 FF FF 7F 61 70 70  32 62 05 80 F8 FF FF 7F  .....app2b......
00E0: F8 FF FF 7F 6D 61 69 6E  06 80 1C 10 80 45 11 80  ....main.....E..
00F0: F0 FF FF 7F F0 FF FF 7F  62 6C 6F 6E 06 80 1C 12  ........blon....
0100: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x00CA [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "app2" with entities [EventEntity, EventEntity], work=551*
  1: 0x00D9 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [EventEntity, EventEntity], work=[78*, 0*]
  2: 0x00EA [0x1C] WAIT(60* ticks)
  3: 0x00ED [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x00FE [0x1C] WAIT(68* ticks)
  5: 0x0101 [0x00] END_REQSTACK()
```
