# 17101377 - Elisabeth

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Caedarva Mire (ID: 79) |
| Block Size       | 88 bytes               |
| Total Events     | 4                      |
| References Count | 7                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [15](#event-15)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     10 |              2 |
| [65535.2](#event-655352) | 0x000C       |     16 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x735B1     |      472497 |
|       1 | 0x12063     |       73827 |
|       2 | 0xFFFF846C  |  4294935660 |
|       3 | 0x072F      |        1839 |
|       4 | 0x733A8     |      471976 |
|       5 | 0x12923     |       76067 |
|       6 | 0xFFFF83EB  |  4294935531 |

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

### Event 15

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
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 00                7.........    
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=472.497*, z=73.827*, y=-31.636*, direction=161.6°*
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      1F 00 04 80              ....
0010: 05 80 06 80 1F 01 1E 42  F2 04 01 00              .......B....    
```

#### Opcodes

```
  0: 0x000C [0x1F] MOVE_ENTITY: EventEntity moves to X=471.976*, Z=76.067*, Y=-31.765*
  1: 0x0014 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0016 [0x1E] EventEntity looks at Iruki-Waraki (ID: 17101378/0x0104F242) and starts talking
  3: 0x001B [0x00] END_REQSTACK()
```
