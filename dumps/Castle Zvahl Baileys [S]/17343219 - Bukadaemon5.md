# 17343219 - Bukadaemon5

## Common Data

| Field            | Value                              |
|------------------|------------------------------------|
| Zone             | Castle Zvahl Baileys [S] (ID: 138) |
| Block Size       | 180 bytes                          |
| Total Events     | 9                                  |
| References Count | 14                                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |      1 |              1 |
| [14](#event-14)          | 0x0002       |      1 |              1 |
| [3](#event-3)            | 0x0003       |      1 |              1 |
| [65535.1](#event-655351) | 0x0004       |     14 |              4 |
| [65535.2](#event-655352) | 0x0012       |     14 |              4 |
| [65535.3](#event-655353) | 0x0020       |     10 |              2 |
| [65535.4](#event-655354) | 0x002A       |     10 |              2 |
| [65535.5](#event-655355) | 0x0034       |     17 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x0580      |        1408 |
|       2 | 0xFFFFFB7B  |  4294966139 |
|       3 | 0xFFFFD8F0  |  4294957296 |
|       4 | 0x0028      |          40 |
|       5 | 0xFFFFFF94  |  4294967188 |
|       6 | 0x0001      |           1 |
|       7 | 0x0000      |           0 |
|       8 | 0x0080      |         128 |
|       9 | 0x005A      |          90 |
|      10 | 0x0044      |          68 |
|      11 | 0x213E1     |      136161 |
|      12 | 0x4FB2      |       20402 |
|      13 | 0xFFFFA232  |  4294943282 |

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

### Event 1

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

### Event 14

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             32 00 80 1F  00 01 80 02 80 03 80 1F      2...........
0010: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0004 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0007 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.408*, Z=-1.157*, Y=-10.000*
  2: 0x000F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0011 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0012   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       32 04 80 1F 00 05  80 06 80 03 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0012 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0015 [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.108*, Z=0.001*, Y=-10.000*
  2: 0x001D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 6C F3 A2 08 01 07 80 06  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0020 [0x6C] FADE_ENTITY_COLOR(entity_id=Bukadaemon5 (ID: 17343219/0x0108A2F3), end_alpha=0*, fade_time=1*)
  1: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                6C F3 A2 08 01 08            l.....
0030: 80 06 80 00                                       ....            
```

#### Opcodes

```
  0: 0x002A [0x6C] FADE_ENTITY_COLOR(entity_id=Bukadaemon5 (ID: 17343219/0x0108A2F3), end_alpha=128*, fade_time=1*)
  1: 0x0033 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0034   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             1C 09 80 32  0A 80 1F 00 0B 80 0C 80      ...2........
0040: 0D 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0034 [0x1C] WAIT(90* ticks)
  1: 0x0037 [0x32] ExtData[1]->MainSpeed = 68* * 0.1
  2: 0x003A [0x1F] MOVE_ENTITY: EventEntity moves to X=136.161*, Z=20.402*, Y=-24.014*
  3: 0x0042 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0044 [0x00] END_REQSTACK()
```
