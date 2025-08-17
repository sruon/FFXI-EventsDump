# 17776645 - Two of Swords

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 236 bytes             |
| Total Events     | 8                     |
| References Count | 11                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |     15 |              4 |
| [33](#event-33)          | 0x000F       |     16 |              2 |
| [34](#event-34)          | 0x001F       |      1 |              1 |
| [65535.1](#event-655351) | 0x0020       |     21 |              3 |
| [65535.2](#event-655352) | 0x0035       |     29 |              3 |
| [65535.3](#event-655353) | 0x0052       |     12 |              4 |
| [65535.4](#event-655354) | 0x005E       |     19 |              3 |
| [65535.5](#event-655355) | 0x0071       |     29 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFF0DCC  |  4294905292 |
|       1 | 0xFFFFE54D  |  4294960461 |
|       2 | 0xFFFFFE0C  |  4294966796 |
|       3 | 0x008B      |         139 |
|       4 | 0x000D      |          13 |
|       5 | 0x00B4      |         180 |
|       6 | 0xFFFFB20E  |  4294947342 |
|       7 | 0x11D69     |       73065 |
|       8 | 0xFFFFE653  |  4294960723 |
|       9 | 0x0205      |         517 |
|      10 | 0x003C      |          60 |

## Events

### Event 65535

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0000   |
| Data Size    | 15 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 22 01 37 00 80 01 80 02  80 03 80 32 04 80 00     ".7........2... 
```

#### Opcodes

```
  0: 0x0000 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-62.004*, z=-6.835*, y=-0.500*, direction=12.2°*
  2: 0x000B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x000E [0x00] END_REQSTACK()
```

### Event 33

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               5B                 [
0010: 05 80 F8 FF FF 7F F8 FF  FF 7F 73 74 64 30 00     ..........std0. 
```

#### Opcodes

```
  0: 0x000F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "std0" with entities [EventEntity, EventEntity], work=180*
  1: 0x001E [0x00] END_REQSTACK()
```

### Event 34

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               00                 .
```

#### Opcodes

```
  0: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 21 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 3B F8 FF FF 7F 00 00 01  00 02 00 37 06 80 07 80  ;..........7....
0030: 08 80 09 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0020 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  1: 0x002B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-19.954*, z=73.065*, y=-6.573*, direction=45.4°*
  2: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                5B 05 80  F8 FF FF 7F F8 FF FF 7F       [..........
0040: 73 74 64 30 53 F8 FF FF  7F F8 FF FF 7F 73 74 64  std0S........std
0050: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0035 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "std0" with entities [EventEntity, EventEntity], work=180*
  1: 0x0044 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "std0" with entities [EventEntity, EventEntity]
  2: 0x0051 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0052   |
| Data Size    | 12 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       37 00 00 01 00 02  00 03 00 6F 70 00          7........op.  
```

#### Opcodes

```
  0: 0x0052 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=ExtData[1]->WorkLocal[2], direction=ExtData[1]->WorkLocal[3]
  1: 0x005B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x005C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005E   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            5B 05                [.
0060: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 62 30 1C 0A 80  .........tlb0...
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x005E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=180*
  1: 0x006D [0x1C] WAIT(60* ticks)
  2: 0x0070 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0071   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    5B 05 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 62 31   [..........tlb1
0080: 53 F8 FF FF 7F F8 FF FF  7F 74 6C 62 31 00        S........tlb1.  
```

#### Opcodes

```
  0: 0x0071 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=180*
  1: 0x0080 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlb1" with entities [EventEntity, EventEntity]
  2: 0x008D [0x00] END_REQSTACK()
```
