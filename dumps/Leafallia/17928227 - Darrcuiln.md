# 17928227 - Darrcuiln

## Common Data

| Field            | Value               |
|------------------|---------------------|
| Zone             | Leafallia (ID: 281) |
| Block Size       | 76 bytes            |
| Total Events     | 4                   |
| References Count | 4                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [12](#event-12)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     17 |              5 |
| [64](#event-64)          | 0x0013       |      7 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0xFFFFC194  |  4294951316 |
|       2 | 0x5108      |       20744 |
|       3 | 0xFFFFFE42  |  4294966850 |

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

### Event 12

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
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 1C    2.............
0010: 00 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 30* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=-15.980*, Z=20.744*, Y=-0.446*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x1C] WAIT(30* ticks)
  4: 0x0012 [0x00] END_REQSTACK()
```

### Event 64

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0013  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          92 01 F8 FF FF  7F 00                       .......      
```

#### Opcodes

```
  0: 0x0013 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0019 [0x00] END_REQSTACK()
```
