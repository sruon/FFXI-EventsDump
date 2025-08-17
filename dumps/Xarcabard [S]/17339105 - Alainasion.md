# 17339105 - Alainasion

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Xarcabard [S] (ID: 137) |
| Block Size       | 284 bytes               |
| Total Events     | 13                      |
| References Count | 21                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [2](#event-2)            | 0x0001       |      1 |              1 |
| [7](#event-7)            | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     14 |              4 |
| [65535.2](#event-655352) | 0x0011       |     11 |              3 |
| [65535.3](#event-655353) | 0x001C       |     10 |              2 |
| [65535.4](#event-655354) | 0x0026       |     10 |              2 |
| [31](#event-31)          | 0x0030       |      1 |              1 |
| [17](#event-17)          | 0x0031       |      1 |              1 |
| [65535.5](#event-655355) | 0x0032       |     26 |              3 |
| [65535.6](#event-655356) | 0x004C       |     21 |              2 |
| [65535.7](#event-655357) | 0x0061       |     21 |              2 |
| [65535.8](#event-655358) | 0x0076       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x533BF     |      340927 |
|       2 | 0xFFFABA33  |  4294621747 |
|       3 | 0xFFFFFB1D  |  4294966045 |
|       4 | 0x52B90     |      338832 |
|       5 | 0xFFFACD94  |  4294626708 |
|       6 | 0xFFFFFD62  |  4294966626 |
|       7 | 0x0000      |           0 |
|       8 | 0x0001      |           1 |
|       9 | 0x0080      |         128 |
|      10 | 0x0003      |           3 |
|      11 | 0x0009      |           9 |
|      12 | 0x0038      |          56 |
|      13 | 0x00DD      |         221 |
|      14 | 0x000C      |          12 |
|      15 | 0x00FB      |         251 |
|      16 | 0x0002      |           2 |
|      17 | 0x001B      |          27 |
|      18 | 0x80C25     |      527397 |
|      19 | 0xFFFBD7EA  |  4294694890 |
|      20 | 0x00C7      |         199 |

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

### Event 2

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

### Event 7

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          32 00 80 1F 00  01 80 02 80 03 80 1F 01     2............
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0003 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0006 [0x1F] MOVE_ENTITY: EventEntity moves to X=340.927*, Z=-345.549*, Y=-1.251*
  2: 0x000E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    1F 00 04 80 05 80 06  80 1F 01 00               ...........    
```

#### Opcodes

```
  0: 0x0011 [0x1F] MOVE_ENTITY: EventEntity moves to X=338.832*, Z=-340.588*, Y=-0.670*
  1: 0x0019 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x001B [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      6C E1 92 08              l...
0020: 01 07 80 08 80 00                                 ......          
```

#### Opcodes

```
  0: 0x001C [0x6C] FADE_ENTITY_COLOR(entity_id=Alainasion (ID: 17339105/0x010892E1), end_alpha=0*, fade_time=1*)
  1: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   6C E1  92 08 01 09 80 08 80 00        l.........
```

#### Opcodes

```
  0: 0x0026 [0x6C] FADE_ENTITY_COLOR(entity_id=Alainasion (ID: 17339105/0x010892E1), end_alpha=128*, fade_time=1*)
  1: 0x002F [0x00] END_REQSTACK()
```

### Event 31

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0030  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0030 [0x00] END_REQSTACK()
```

### Event 17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0031  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    00                                              .              
```

#### Opcodes

```
  0: 0x0031 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0032   |
| Data Size    | 26 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       B6 0B 0A 80 0B 80  0C 80 0D 80 0E 80 0E 80    ..............
0040: 0E 80 0F 80 07 80 80 E1  92 08 01 00              ............    
```

#### Opcodes

```
  0: 0x0032 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=9*, head=56*, body=221*, hands=12*, legs=12*, feet=12*, main=251*, sub=0*)
  1: 0x0046 [0x80] LOAD_WAIT(entity=Alainasion (ID: 17339105/0x010892E1))
  2: 0x004B [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004C   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      B6 0B 08 80              ....
0050: 0B 80 10 80 10 80 10 80  10 80 10 80 0F 80 07 80  ................
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x004C [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=9*, head=2*, body=2*, hands=2*, legs=2*, feet=2*, main=251*, sub=0*)
  1: 0x0060 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0061   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:    B6 0B 0A 80 0A 80 00  80 0D 80 00 80 0E 80 0D   ...............
0070: 80 0F 80 11 80 00                                 ......          
```

#### Opcodes

```
  0: 0x0061 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=3*, head=13*, body=221*, hands=13*, legs=12*, feet=221*, main=251*, sub=27*)
  1: 0x0075 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0076   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                   32 00  80 1F 00 12 80 13 80 14        2.........
0080: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0076 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0079 [0x1F] MOVE_ENTITY: EventEntity moves to X=527.397*, Z=-272.406*, Y=0.199*
  2: 0x0081 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0083 [0x00] END_REQSTACK()
```
