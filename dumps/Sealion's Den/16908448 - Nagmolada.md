# 16908448 - Nagmolada

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Sealion's Den (ID: 32) |
| Block Size       | 448 bytes              |
| Total Events     | 16                     |
| References Count | 20                     |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |     13 |              3 |
| [2](#event-2)              | 0x000D       |     10 |              2 |
| [65535.1](#event-655351)   | 0x0017       |     67 |             13 |
| [33](#event-33)            | 0x005A       |     10 |              2 |
| [65535.2](#event-655352)   | 0x0064       |     14 |              4 |
| [65535.3](#event-655353)   | 0x0072       |     14 |              4 |
| [65535.4](#event-655354)   | 0x0080       |     16 |              2 |
| [65535.5](#event-655355)   | 0x0090       |     16 |              2 |
| [65535.6](#event-655356)   | 0x00A0       |     16 |              2 |
| [65535.7](#event-655357)   | 0x00B0       |     16 |              2 |
| [65535.8](#event-655358)   | 0x00C0       |     16 |              2 |
| [65535.9](#event-655359)   | 0x00D0       |     16 |              2 |
| [65535.10](#event-6553510) | 0x00E0       |     16 |              2 |
| [65535.11](#event-6553511) | 0x00F0       |     16 |              2 |
| [65535.12](#event-6553512) | 0x0100       |     16 |              2 |
| [65535.13](#event-6553513) | 0x0110       |     16 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFF63C08  |  4294327304 |
|       1 | 0x7C235     |      508469 |
|       2 | 0xFFFC6BCE  |  4294732750 |
|       3 | 0x0BC3      |        3011 |
|       4 | 0x0005      |           5 |
|       5 | 0x0040      |          64 |
|       6 | 0x0001      |           1 |
|       7 | 0x0800      |        2048 |
|       8 | 0xFFF63BA6  |  4294327206 |
|       9 | 0x7BF1B     |      507675 |
|      10 | 0x0DA8      |        3496 |
|      11 | 0x000D      |          13 |
|      12 | 0xFFF63BC0  |  4294327232 |
|      13 | 0x7C060     |      508000 |
|      14 | 0xFFF63C4F  |  4294327375 |
|      15 | 0x85DFC     |      548348 |
|      16 | 0xFFFC4DE8  |  4294725096 |
|      17 | 0x0C00      |        3072 |
|      18 | 0x01D1      |         465 |
|      19 | 0x01D3      |         467 |

## Events

### Event 65535

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0000   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 92 01 F8 FF FF 7F 94 01  F8 FF FF 7F 00           .............   
```

#### Opcodes

```
  0: 0x0000 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000C [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         37 00 80               7..
0010: 01 80 02 80 03 80 00                              .......         
```

#### Opcodes

```
  0: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-639.992*, z=508.469*, y=-234.546*, direction=264.6°*
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 67 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      33  01 3B F8 FF FF 7F 00 00         3.;......
0020: 01 00 02 00 06 05 00 16  04 00 05 00 04 80 07 02  ................
0030: 00 04 00 3A F8 FF FF 7F  03 00 37 00 00 01 00 02  ...:......7.....
0040: 00 03 00 07 05 00 05 80  1C 06 80 01 27 00 02 05  ............'...
0050: 00 07 80 04 59 00 06 05  00 00                    ....Y.....      
```

#### Opcodes

```
  0: 0x0017 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0019 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  2: 0x0024 [0x06] ExtData[1]->WorkLocal[5] = 0
  3: 0x0027 [0x16] ExtData[1]->WorkLocal[4] = sin(ExtData[1]->WorkLocal[5]) * 5*
  4: 0x002E [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[4]
  5: 0x0033 [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[3])
  6: 0x003A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=ExtData[1]->WorkLocal[2], direction=ExtData[1]->WorkLocal[3]
  7: 0x0043 [0x07] ExtData[1]->WorkLocal[5] += 64*
  8: 0x0048 [0x1C] WAIT(1* ticks)
  9: 0x004B [0x01] GOTO 0x0027
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x004E [0x02] IF !(ExtData[1]->WorkLocal[5] < 2048*) GOTO 0x0059
     0x0056 [0x06] ExtData[1]->WorkLocal[5] = 0
     0x0059 [0x00] END_REQSTACK()
```

### Event 33

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                37 08 80 09 80 02            7.....
0060: 80 0A 80 00                                       ....            
```

#### Opcodes

```
  0: 0x005A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-640.090*, z=507.675*, y=-234.546*, direction=307.3°*
  1: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0064   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             32 0B 80 1F  00 0C 80 0D 80 02 80 1F      2...........
0070: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0064 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0067 [0x1F] MOVE_ENTITY: EventEntity moves to X=-640.064*, Z=508.000*, Y=-234.546*
  2: 0x006F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0071 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0072   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       33 01 A5 01 37 0E  80 0F 80 10 80 11 80 00    3...7.........
```

#### Opcodes

```
  0: 0x0072 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0074 [0xA5] EventEntity->Flags3.BallistaTeam |= 0x08  // Set bit 3 of BallistaTeam
  2: 0x0076 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-639.921*, z=548.348*, y=-242.200*, direction=270.0°*
  3: 0x007F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0080   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080: 5B 12 80 F8 FF FF 7F F8  FF FF 7F 74 6C 61 30 00  [..........tla0.
```

#### Opcodes

```
  0: 0x0080 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla0" with entities [EventEntity, EventEntity], work=465*
  1: 0x008F [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0090   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090: 5B 12 80 F8 FF FF 7F F8  FF FF 7F 74 6C 61 31 00  [..........tla1.
```

#### Opcodes

```
  0: 0x0090 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla1" with entities [EventEntity, EventEntity], work=465*
  1: 0x009F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A0   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0: 5B 12 80 F8 FF FF 7F F8  FF FF 7F 74 6C 62 30 00  [..........tlb0.
```

#### Opcodes

```
  0: 0x00A0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=465*
  1: 0x00AF [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B0   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0: 5B 12 80 F8 FF FF 7F F8  FF FF 7F 74 6C 62 31 00  [..........tlb1.
```

#### Opcodes

```
  0: 0x00B0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=465*
  1: 0x00BF [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C0   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0: 5B 12 80 F8 FF FF 7F F8  FF FF 7F 74 61 62 30 00  [..........tab0.
```

#### Opcodes

```
  0: 0x00C0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tab0" with entities [EventEntity, EventEntity], work=465*
  1: 0x00CF [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D0   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0: 5B 12 80 F8 FF FF 7F F8  FF FF 7F 74 62 61 30 00  [..........tba0.
```

#### Opcodes

```
  0: 0x00D0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tba0" with entities [EventEntity, EventEntity], work=465*
  1: 0x00DF [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E0   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0: 5B 13 80 F8 FF FF 7F F8  FF FF 7F 73 6E 62 30 00  [..........snb0.
```

#### Opcodes

```
  0: 0x00E0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "snb0" with entities [EventEntity, EventEntity], work=467*
  1: 0x00EF [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F0   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0: 5B 13 80 F8 FF FF 7F F8  FF FF 7F 73 6E 62 31 00  [..........snb1.
```

#### Opcodes

```
  0: 0x00F0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "snb1" with entities [EventEntity, EventEntity], work=467*
  1: 0x00FF [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0100   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100: 5B 12 80 F8 FF FF 7F F8  FF FF 7F 74 68 62 30 00  [..........thb0.
```

#### Opcodes

```
  0: 0x0100 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thb0" with entities [EventEntity, EventEntity], work=465*
  1: 0x010F [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0110   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110: 5B 12 80 F8 FF FF 7F F8  FF FF 7F 74 68 62 31 00  [..........thb1.
```

#### Opcodes

```
  0: 0x0110 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thb1" with entities [EventEntity, EventEntity], work=465*
  1: 0x011F [0x00] END_REQSTACK()
```
