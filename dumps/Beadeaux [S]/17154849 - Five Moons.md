# 17154849 - Five Moons

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Beadeaux [S] (ID: 92) |
| Block Size       | 176 bytes             |
| Total Events     | 8                     |
| References Count | 10                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     19 |              5 |
| [65535.2](#event-655352) | 0x0015       |     19 |              5 |
| [65535.3](#event-655353) | 0x0028       |     14 |              3 |
| [65535.4](#event-655354) | 0x0036       |     14 |              3 |
| [65535.5](#event-655355) | 0x0044       |     10 |              2 |
| [65535.6](#event-655356) | 0x004E       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0xFFFCAC3D  |  4294749245 |
|       2 | 0xF27C      |       62076 |
|       3 | 0x03E7      |         999 |
|       4 | 0x001E      |          30 |
|       5 | 0x0102      |         258 |
|       6 | 0x0078      |         120 |
|       7 | 0x0000      |           0 |
|       8 | 0x0001      |           1 |
|       9 | 0x0080      |         128 |

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 1E    2.............
0010: 23 C3 05 01 00                                    #....           
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=-218.051*, Z=62.076*, Y=0.999*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x1E] EventEntity looks at Rainer (ID: 17154851/0x0105C323) and starts talking
  4: 0x0014 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0015   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                1C 04 80  6E 21 C3 05 01 05 80 99       ...n!......
0020: 21 C3 05 01 1C 06 80 00                           !.......        
```

#### Opcodes

```
  0: 0x0015 [0x1C] WAIT(30* ticks)
  1: 0x0018 [0x6E] Five Moons (ID: 17154849/0x0105C321) uses emote 258*
  2: 0x001F [0x99] Wait for Five Moons (ID: 17154849/0x0105C321) animation to complete
  3: 0x0024 [0x1C] WAIT(120* ticks)
  4: 0x0027 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0028   |
| Data Size    | 14 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          1C 04 80 79 00 21 C3 05          ...y.!..
0030: 01 23 C3 05 01 00                                 .#....          
```

#### Opcodes

```
  0: 0x0028 [0x1C] WAIT(30* ticks)
  1: 0x002B [0x79] Five Moons (ID: 17154849/0x0105C321) looks at Rainer (ID: 17154851/0x0105C323) (Basic look)
  2: 0x0035 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0036   |
| Data Size    | 14 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   1C 04  80 79 00 21 C3 05 01 20        ...y.!... 
0040: C3 05 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0036 [0x1C] WAIT(30* ticks)
  1: 0x0039 [0x79] Five Moons (ID: 17154849/0x0105C321) looks at Nicolaus (ID: 17154848/0x0105C320) (Basic look)
  2: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             6C 21 C3 05  01 07 80 08 80 00            l!........  
```

#### Opcodes

```
  0: 0x0044 [0x6C] FADE_ENTITY_COLOR(entity_id=Five Moons (ID: 17154849/0x0105C321), end_alpha=0*, fade_time=1*)
  1: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            6C 21                l!
0050: C3 05 01 09 80 08 80 00                           ........        
```

#### Opcodes

```
  0: 0x004E [0x6C] FADE_ENTITY_COLOR(entity_id=Five Moons (ID: 17154849/0x0105C321), end_alpha=128*, fade_time=1*)
  1: 0x0057 [0x00] END_REQSTACK()
```
