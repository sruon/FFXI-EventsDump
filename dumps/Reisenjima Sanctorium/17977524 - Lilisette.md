# 17977524 - Lilisette

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Reisenjima Sanctorium (ID: 293) |
| Block Size       | 128 bytes                       |
| Total Events     | 8                               |
| References Count | 8                               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [11](#event-11)          | 0x0001       |      4 |              2 |
| [65535.1](#event-655351) | 0x0005       |     14 |              4 |
| [65535.2](#event-655352) | 0x0013       |     10 |              2 |
| [65535.3](#event-655353) | 0x001D       |      5 |              2 |
| [65535.4](#event-655354) | 0x0022       |      5 |              2 |
| [65535.5](#event-655355) | 0x0027       |      3 |              2 |
| [65535.6](#event-655356) | 0x002A       |      3 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0028      |          40 |
|       2 | 0xFFFFE2A3  |  4294959779 |
|       3 | 0xFFFFF9AB  |  4294965675 |
|       4 | 0x0EA7      |        3751 |
|       5 | 0x0000      |           0 |
|       6 | 0x08E7      |        2279 |
|       7 | 0x0C4F      |        3151 |

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

### Event 11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    C0 00 80 00                                     ....           
```

#### Opcodes

```
  0: 0x0001 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x0004 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0005   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                32 01 80  1F 00 02 80 03 80 04 80       2..........
0010: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0005 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0008 [0x1F] MOVE_ENTITY: EventEntity moves to X=-7.517*, Z=-1.621*, Y=3.751*
  2: 0x0010 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0012 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0013   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          6C F8 FF FF 7F  05 80 00 80 00              l.........   
```

#### Opcodes

```
  0: 0x0013 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001D  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         B6 00 06               ...
0020: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x001D [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2279*)
  1: 0x0021 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0022  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       B6 00 07 80 00                                .....         
```

#### Opcodes

```
  0: 0x0022 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=3151*)
  1: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      AB  08 00                           ...      
```

#### Opcodes

```
  0: 0x0027 [0xAB] EventEntity->Render.Flags2 |= 0x02 // Set bit 1
  1: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002A  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                AB 07 00                     ...   
```

#### Opcodes

```
  0: 0x002A [0xAB] EventEntity->Render.Flags2 |= 0x01 // Set bit 0
  1: 0x002C [0x00] END_REQSTACK()
```
