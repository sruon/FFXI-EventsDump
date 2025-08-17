# 17723431 - Cauzeriste

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 152 bytes                     |
| Total Events     | 5                             |
| References Count | 12                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [535](#event-535)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     10 |              2 |
| [16](#event-16)          | 0x000C       |     28 |              5 |
| [0](#event-0)            | 0x0028       |     28 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFDD2FD  |  4294824701 |
|       1 | 0x308AC     |      198828 |
|       2 | 0x2EDF      |       11999 |
|       3 | 0x0104      |         260 |
|       4 | 0x14F3F     |       85823 |
|       5 | 0x15161     |       86369 |
|       6 | 0x06D5      |        1749 |
|       7 | 0x0FF6      |        4086 |
|       8 | 0xFFFFDCA3  |  4294958243 |
|       9 | 0x17C76     |       97398 |
|      10 | 0xFFFFFF39  |  4294967097 |
|      11 | 0x0E20      |        3616 |

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

### Event 535

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
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-142.595*, z=198.828*, y=11.999*, direction=22.9°*
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 28 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      22 00 92 01              "...
0010: F8 FF FF 7F 37 04 80 05  80 06 80 07 80 79 00 F8  ....7........y..
0020: FF FF 7F 04 70 0E 01 00                           ....p...        
```

#### Opcodes

```
  0: 0x000C [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x000E [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0014 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=85.823*, z=86.369*, y=1.749*, direction=359.1°*
  3: 0x001D [0x79] EventEntity looks at Claidie (ID: 17723396/0x010E7004) (Basic look)
  4: 0x0027 [0x00] END_REQSTACK()
```

### Event 0

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0028   |
| Data Size    | 28 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          22 00 92 01 F8 FF FF 7F          ".......
0030: 37 08 80 09 80 0A 80 0B  80 79 00 F8 FF FF 7F 02  7........y......
0040: 70 0E 01 00                                       p...            
```

#### Opcodes

```
  0: 0x0028 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x002A [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0030 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-9.053*, z=97.398*, y=-0.199*, direction=317.8°*
  3: 0x0039 [0x79] EventEntity looks at Trion (ID: 17723394/0x010E7002) (Basic look)
  4: 0x0043 [0x00] END_REQSTACK()
```
