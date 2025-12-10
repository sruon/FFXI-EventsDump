# 17269308 - Lilisette

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Sauromugue Champaign (ID: 120) |
| Block Size       | 84 bytes                       |
| Total Events     | 4                              |
| References Count | 6                              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [20](#event-20)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     10 |              2 |
| [65535.2](#event-655352) | 0x000C       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0080      |         128 |
|       1 | 0x0001      |           1 |
|       2 | 0x0028      |          40 |
|       3 | 0xFFF99218  |  4294545944 |
|       4 | 0xFFFCC840  |  4294756416 |
|       5 | 0x4E1F      |       19999 |

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

### Event 20

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
0000:       6C F8 FF FF 7F 00  80 01 80 00                l.........    
```

#### Opcodes

```
  0: 0x0002 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      32 02 80 1F              2...
0010: 00 03 80 04 80 05 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x000C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=-421.352*, Z=-210.880*, Y=19.999*
  2: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0019 [0x00] END_REQSTACK()
```
