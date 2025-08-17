# 17375831 - Black Dragon

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Balga's Dais (ID: 146) |
| Block Size       | 116 bytes              |
| Total Events     | 4                      |
| References Count | 9                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [32000](#event-32000)    | 0x0001       |     16 |              3 |
| [32001](#event-32001)    | 0x0011       |     10 |              2 |
| [65535.1](#event-655351) | 0x001B       |     19 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0xFFFDF400  |  4294833152 |
|       3 | 0xFFFC8A2E  |  4294740526 |
|       4 | 0xDC5F      |       56415 |
|       5 | 0x0A9F      |        2719 |
|       6 | 0x001E      |          30 |
|       7 | 0x007F      |         127 |
|       8 | 0x010E      |         270 |

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

### Event 32000

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 6C  F8 FF FF 7F 00 80 01 80   ......l........
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  2: 0x0010 [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    37 02 80 03 80 04 80  05 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0011 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-134.144*, z=-226.770*, y=56.415*, direction=239.0°*
  1: 0x001A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 19 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   1C 06 80 92 00             .....
0020: F8 FF FF 7F 6C F8 FF FF  7F 07 80 08 80 00        ....l.........  
```

#### Opcodes

```
  0: 0x001B [0x1C] WAIT(30* ticks)
  1: 0x001E [0x92] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  2: 0x0024 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=127*, fade_time=270*)
  3: 0x002D [0x00] END_REQSTACK()
```
