# 17768550 - Karaha-Baruha

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Heavens Tower (ID: 242) |
| Block Size       | 208 bytes               |
| Total Events     | 8                       |
| References Count | 14                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     14 |              2 |
| [362](#event-362)        | 0x001F       |      7 |              2 |
| [65535.3](#event-655353) | 0x0026       |     10 |              2 |
| [65535.4](#event-655354) | 0x0030       |     10 |              2 |
| [65535.5](#event-655355) | 0x003A       |     21 |              7 |
| [65535.6](#event-655356) | 0x004F       |     23 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x025C      |         604 |
|       1 | 0x2AF9      |       11001 |
|       2 | 0x10B1B     |       68379 |
|       3 | 0xFFFF0FC4  |  4294905796 |
|       4 | 0x0FA3      |        4003 |
|       5 | 0xFFFF15A0  |  4294907296 |
|       6 | 0xF230      |       62000 |
|       7 | 0x24A7      |        9383 |
|       8 | 0x0C71      |        3185 |
|       9 | 0x000D      |          13 |
|      10 | 0x61BA      |       25018 |
|      11 | 0x107EC     |       67564 |
|      12 | 0x6C80      |       27776 |
|      13 | 0x10C7C     |       68732 |

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
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 6D 67 63 30   [..........mgc0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "mgc0" with entities [EventEntity, EventEntity], work=604*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 6D 67 63 30 00      S........mgc0. 
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "mgc0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x00] END_REQSTACK()
```

### Event 362

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001F  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               92                 .
0020: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x001F [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   37 01  80 02 80 03 80 04 80 00        7.........
```

#### Opcodes

```
  0: 0x0026 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=11.001*, z=68.379*, y=-61.500*, direction=351.8°*
  1: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 37 05 80 06 80 07 80 08  80 00                    7.........      
```

#### Opcodes

```
  0: 0x0030 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-60.000*, z=62.000*, y=9.383*, direction=279.9°*
  1: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 21 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                32 09 80 1F 00 0A            2.....
0040: 80 0B 80 03 80 1F 01 1E  1D 20 0F 01 6F 70 00     ......... ..op. 
```

#### Opcodes

```
  0: 0x003A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003D [0x1F] MOVE_ENTITY: EventEntity moves to X=25.018*, Z=67.564*, Y=-61.500*
  2: 0x0045 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0047 [0x1E] EventEntity looks at Star Sibyl (ID: 17768477/0x010F201D) and starts talking
  4: 0x004C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x004D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x004E [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004F   |
| Data Size    | 23 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               32                 2
0050: 09 80 33 01 1F 00 0C 80  0D 80 03 80 1F 01 1E 1D  ..3.............
0060: 20 0F 01 6F 70 00                                  ..op.          
```

#### Opcodes

```
  0: 0x004F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0052 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  2: 0x0054 [0x1F] MOVE_ENTITY: EventEntity moves to X=27.776*, Z=68.732*, Y=-61.500*
  3: 0x005C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x005E [0x1E] EventEntity looks at Star Sibyl (ID: 17768477/0x010F201D) and starts talking
  5: 0x0063 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0064 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x0065 [0x00] END_REQSTACK()
```
