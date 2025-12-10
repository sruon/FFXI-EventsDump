# 17293781 - Seed Mandragora

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Qufim Island (ID: 126) |
| Block Size       | 252 bytes              |
| Total Events     | 12                     |
| References Count | 18                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [31](#event-31)          | 0x0001       |      4 |              2 |
| [65535.1](#event-655351) | 0x0005       |     20 |              5 |
| [65535.2](#event-655352) | 0x0019       |     20 |              5 |
| [65535.3](#event-655353) | 0x002D       |      5 |              2 |
| [65535.4](#event-655354) | 0x0032       |      5 |              2 |
| [65535.5](#event-655355) | 0x0037       |      5 |              2 |
| [32](#event-32)          | 0x003C       |      4 |              2 |
| [65535.6](#event-655356) | 0x0040       |     20 |              5 |
| [65535.7](#event-655357) | 0x0054       |     20 |              5 |
| [65535.8](#event-655358) | 0x0068       |      5 |              2 |
| [34](#event-34)          | 0x006D       |      4 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x000D      |          13 |
|       2 | 0x58F6      |       22774 |
|       3 | 0x43D17     |      277783 |
|       4 | 0xFFFFAC13  |  4294945811 |
|       5 | 0xFFFF2D84  |  4294913412 |
|       6 | 0x3A30E     |      238350 |
|       7 | 0xFFFF5FD8  |  4294926296 |
|       8 | 0x02C4      |         708 |
|       9 | 0x002A      |          42 |
|      10 | 0x012C      |         300 |
|      11 | 0xFFFE0760  |  4294838112 |
|      12 | 0x48047     |      294983 |
|      13 | 0xFFFFB3E3  |  4294947811 |
|      14 | 0x0028      |          40 |
|      15 | 0xFFFE1188  |  4294840712 |
|      16 | 0x48BFF     |      297983 |
|      17 | 0x0930      |        2352 |

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

### Event 31

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
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                59 04 D5  E1 07 01 01 80 1F 00 02       Y..........
0010: 80 03 80 04 80 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x0005 [0x59] UPDATE_ENTITY_DATA: Set Seed Mandragora (ID: 17293781/0x0107E1D5) main speed = 13* * 0.1
  1: 0x000D [0x1F] MOVE_ENTITY: EventEntity moves to X=22.774*, Z=277.783*, Y=-21.485*
  2: 0x0015 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0017 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0018 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             59 04 D5 E1 07 01 01           Y......
0020: 80 1F 00 05 80 06 80 07  80 1F 01 6F 00           ...........o.   
```

#### Opcodes

```
  0: 0x0019 [0x59] UPDATE_ENTITY_DATA: Set Seed Mandragora (ID: 17293781/0x0107E1D5) main speed = 13* * 0.1
  1: 0x0021 [0x1F] MOVE_ENTITY: EventEntity moves to X=-53.884*, Z=238.350*, Y=-41.000*
  2: 0x0029 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002D  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         B6 00 08               ...
0030: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x002D [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=708*)
  1: 0x0031 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0032  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       B6 00 09 80 00                                .....         
```

#### Opcodes

```
  0: 0x0032 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=42*)
  1: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0037  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      B6  00 0A 80 00                     .....    
```

#### Opcodes

```
  0: 0x0037 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=300*)
  1: 0x003B [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003C  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      C0 00 80 00              ....
```

#### Opcodes

```
  0: 0x003C [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x003F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0040   |
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: 59 04 D5 E1 07 01 01 80  1F 00 0B 80 0C 80 0D 80  Y...............
0050: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x0040 [0x59] UPDATE_ENTITY_DATA: Set Seed Mandragora (ID: 17293781/0x0107E1D5) main speed = 13* * 0.1
  1: 0x0048 [0x1F] MOVE_ENTITY: EventEntity moves to X=-129.184*, Z=294.983*, Y=-19.485*
  2: 0x0050 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0052 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0053 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             59 04 D5 E1  07 01 0E 80 1F 00 0F 80      Y...........
0060: 10 80 0D 80 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x0054 [0x59] UPDATE_ENTITY_DATA: Set Seed Mandragora (ID: 17293781/0x0107E1D5) main speed = 40* * 0.1
  1: 0x005C [0x1F] MOVE_ENTITY: EventEntity moves to X=-126.584*, Z=297.983*, Y=-19.485*
  2: 0x0064 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0066 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0067 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0068  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                          B6 00 11 80 00                   .....   
```

#### Opcodes

```
  0: 0x0068 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2352*)
  1: 0x006C [0x00] END_REQSTACK()
```

### Event 34

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006D  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         C0 00 80               ...
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x006D [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x0070 [0x00] END_REQSTACK()
```
