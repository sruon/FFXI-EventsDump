# 17793105 - Mitsunari

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Selbina (ID: 248) |
| Block Size       | 140 bytes         |
| Total Events     | 4                 |
| References Count | 13                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1101](#event-1101)      | 0x0001       |     21 |              4 |
| [65535.1](#event-655351) | 0x0016       |     12 |              3 |
| [65535.2](#event-655352) | 0x0022       |     21 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x46DD      |       18141 |
|       1 | 0xFFFF5AF4  |  4294925044 |
|       2 | 0xFFFFF602  |  4294964738 |
|       3 | 0x0AEE      |        2798 |
|       4 | 0x0000      |           0 |
|       5 | 0x0001      |           1 |
|       6 | 0x0048      |          72 |
|       7 | 0x003C      |          60 |
|       8 | 0x0080      |         128 |
|       9 | 0xFFFFC3CE  |  4294951886 |
|      10 | 0xFFFF86AE  |  4294936238 |
|      11 | 0xFFFFFCB8  |  4294966456 |
|      12 | 0x03FE      |        1022 |

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

### Event 1101

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 21 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    22 01 37 00 80 01 80  02 80 03 80 6C F8 FF FF   ".7........l...
0010: 7F 04 80 05 80 00                                 ......          
```

#### Opcodes

```
  0: 0x0001 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0003 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=18.141*, z=-42.252*, y=-2.558*, direction=245.9°*
  2: 0x000C [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   22 00  6C F8 FF FF 7F 06 80 07        ".l.......
0020: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0016 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0018 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=72*, fade_time=60*)
  2: 0x0021 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0022   |
| Data Size    | 21 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       22 00 6C F8 FF FF  7F 08 80 05 80 37 09 80    ".l........7..
0030: 0A 80 0B 80 0C 80 00                              .......         
```

#### Opcodes

```
  0: 0x0022 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0024 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  2: 0x002D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-15.410*, z=-31.058*, y=-0.840*, direction=89.8°*
  3: 0x0036 [0x00] END_REQSTACK()
```
