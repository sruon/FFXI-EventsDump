# 17339047 - Slumbering Savage

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Xarcabard [S] (ID: 137) |
| Block Size       | 224 bytes               |
| Total Events     | 8                       |
| References Count | 19                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [8](#event-8)            | 0x0001       |      7 |              2 |
| [9](#event-9)            | 0x0008       |      7 |              2 |
| [65535.1](#event-655351) | 0x000F       |     14 |              4 |
| [10](#event-10)          | 0x001D       |      7 |              2 |
| [65535.2](#event-655352) | 0x0024       |     14 |              4 |
| [65535.3](#event-655353) | 0x0032       |     34 |              8 |
| [65535.4](#event-655354) | 0x0054       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x24FFE     |      151550 |
|       2 | 0xFFFF22D6  |  4294910678 |
|       3 | 0x0141      |         321 |
|       4 | 0x26AC0     |      158400 |
|       5 | 0xFFFF16F5  |  4294907637 |
|       6 | 0x04BB      |        1211 |
|       7 | 0x24753     |      149331 |
|       8 | 0xFFFF1FBA  |  4294909882 |
|       9 | 0x01E6      |         486 |
|      10 | 0x23DC9     |      146889 |
|      11 | 0xFFFF2582  |  4294911362 |
|      12 | 0x02C9      |         713 |
|      13 | 0x23012     |      143378 |
|      14 | 0xFFFF33DC  |  4294915036 |
|      15 | 0x04B9      |        1209 |
|      16 | 0x22228     |      139816 |
|      17 | 0xFFFF7687  |  4294932103 |
|      18 | 0x0478      |        1144 |

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

### Event 8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0008 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               32                 2
0010: 00 80 1F 00 01 80 02 80  03 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x000F [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0012 [0x1F] MOVE_ENTITY: EventEntity moves to X=151.550*, Z=-56.618*, Y=0.321*
  2: 0x001A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001C [0x00] END_REQSTACK()
```

### Event 10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001D  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         92 01 F8               ...
0020: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x001D [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             32 00 80 1F  00 04 80 05 80 06 80 1F      2...........
0030: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0024 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0027 [0x1F] MOVE_ENTITY: EventEntity moves to X=158.400*, Z=-59.659*, Y=1.211*
  2: 0x002F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0031 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0032   |
| Data Size    | 34 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       32 00 80 1F 00 07  80 08 80 09 80 1F 01 1F    2.............
0040: 00 0A 80 0B 80 0C 80 1F  01 1F 00 0D 80 0E 80 0F  ................
0050: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0032 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0035 [0x1F] MOVE_ENTITY: EventEntity moves to X=149.331*, Z=-57.414*, Y=0.486*
  2: 0x003D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003F [0x1F] MOVE_ENTITY: EventEntity moves to X=146.889*, Z=-55.934*, Y=0.713*
  4: 0x0047 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0049 [0x1F] MOVE_ENTITY: EventEntity moves to X=143.378*, Z=-52.260*, Y=1.209*
  6: 0x0051 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0053 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             32 00 80 1F  00 10 80 11 80 12 80 1F      2...........
0060: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0054 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0057 [0x1F] MOVE_ENTITY: EventEntity moves to X=139.816*, Z=-35.193*, Y=1.144*
  2: 0x005F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0061 [0x00] END_REQSTACK()
```
