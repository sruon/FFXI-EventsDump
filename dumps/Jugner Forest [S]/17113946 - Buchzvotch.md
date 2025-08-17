# 17113946 - Buchzvotch

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Jugner Forest [S] (ID: 82) |
| Block Size       | 168 bytes                  |
| Total Events     | 9                          |
| References Count | 12                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [204](#event-204)        | 0x0001       |      1 |              1 |
| [205](#event-205)        | 0x0002       |      1 |              1 |
| [206](#event-206)        | 0x0003       |      1 |              1 |
| [65535.1](#event-655351) | 0x0004       |      4 |              2 |
| [65535.2](#event-655352) | 0x0008       |     24 |              6 |
| [65535.3](#event-655353) | 0x0020       |     15 |              5 |
| [65535.4](#event-655354) | 0x002F       |     10 |              2 |
| [65535.5](#event-655355) | 0x0039       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x0028      |          40 |
|       2 | 0xFFFFF107  |  4294963463 |
|       3 | 0xFFFB39A8  |  4294654376 |
|       4 | 0xFFFFFFF4  |  4294967284 |
|       5 | 0x02DD      |         733 |
|       6 | 0xFFFFEF14  |  4294962964 |
|       7 | 0xFFFB2DF5  |  4294651381 |
|       8 | 0x0007      |           7 |
|       9 | 0x0000      |           0 |
|      10 | 0x0001      |           1 |
|      11 | 0x0080      |         128 |

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

### Event 204

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

### Event 205

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

### Event 206

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0004  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             32 00 80 00                               2...        
```

#### Opcodes

```
  0: 0x0004 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          32 01 80 37 02 80 03 80          2..7....
0010: 04 80 05 80 1F 00 06 80  07 80 08 80 1F 01 6F 00  ..............o.
```

#### Opcodes

```
  0: 0x0008 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x000B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-3.833*, z=-312.920*, y=-0.012*, direction=64.4°*
  2: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=-4.332*, Z=-315.915*, Y=0.007*
  3: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x001E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 32 00 80 1F 00 25 10 27  10 26 10 1F 01 6F 00     2....%.'.&...o. 
```

#### Opcodes

```
  0: 0x0020 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0023 [0x1F] MOVE_ENTITY: EventEntity moves to X=Work_Zone[37], Z=Work_Zone[39], Y=Work_Zone[38]
  2: 0x002B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               6C                 l
0030: 5A 23 05 01 09 80 0A 80  00                       Z#.......       
```

#### Opcodes

```
  0: 0x002F [0x6C] FADE_ENTITY_COLOR(entity_id=Buchzvotch (ID: 17113946/0x0105235A), end_alpha=0*, fade_time=1*)
  1: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             6C 5A 23 05 01 0B 80           lZ#....
0040: 0A 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0039 [0x6C] FADE_ENTITY_COLOR(entity_id=Buchzvotch (ID: 17113946/0x0105235A), end_alpha=128*, fade_time=1*)
  1: 0x0042 [0x00] END_REQSTACK()
```
