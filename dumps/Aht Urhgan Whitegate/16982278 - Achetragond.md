# 16982278 - Achetragond

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Aht Urhgan Whitegate (ID: 50) |
| Block Size       | 320 bytes                     |
| Total Events     | 9                             |
| References Count | 28                            |

## List of Events

| Event ID                  | Entrypoint   |   Size |   Instructions |
|---------------------------|--------------|--------|----------------|
| [65535](#event-65535)     | 0x0000       |      1 |              1 |
| [686](#event-686)         | 0x0001       |      1 |              1 |
| [690](#event-690)         | 0x0002       |      1 |              1 |
| [65535.1](#event-65535-1) | 0x0003       |     30 |              3 |
| [65535.2](#event-65535-2) | 0x0021       |     30 |              3 |
| [65535.3](#event-65535-3) | 0x003F       |     30 |              3 |
| [65535.4](#event-65535-4) | 0x005D       |     38 |              5 |
| [65535.5](#event-65535-5) | 0x0083       |      9 |              3 |
| [65535.6](#event-65535-6) | 0x008C       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0008      |           8 |
|       1 | 0x0007      |           7 |
|       2 | 0x000F      |          15 |
|       3 | 0x00FB      |         251 |
|       4 | 0xFFFF437C  |  4294919036 |
|       5 | 0x13116     |       78102 |
|       6 | 0x0000      |           0 |
|       7 | 0x0075      |         117 |
|       8 | 0x0001      |           1 |
|       9 | 0x000B      |          11 |
|      10 | 0x0014      |          20 |
|      11 | 0xFFFF1C1D  |  4294908957 |
|      12 | 0x182E4     |       99044 |
|      13 | 0x0D19      |        3353 |
|      14 | 0x0002      |           2 |
|      15 | 0x0004      |           4 |
|      16 | 0x0036      |          54 |
|      17 | 0x7052      |       28754 |
|      18 | 0xFFFE1058  |  4294840408 |
|      19 | 0xFFFFE890  |  4294961296 |
|      20 | 0x0441      |        1089 |
|      21 | 0xFFFE6B40  |  4294863680 |
|      22 | 0xFFFFAC40  |  4294945856 |
|      23 | 0x0287      |         647 |
|      24 | 0x0003      |           3 |
|      25 | 0x0028      |          40 |
|      26 | 0xFFFE8602  |  4294870530 |
|      27 | 0xFFFFAE4B  |  4294946379 |

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

### Event 686

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

### Event 690

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
| Data Size    | 30 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          B6 0B 00 80 01  80 02 80 02 80 02 80 02     .............
0010: 80 02 80 03 80 02 80 37  04 80 05 80 06 80 07 80  .......7........
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0003 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=8*, hair=7*, head=15*, body=15*, hands=15*, legs=15*, feet=15*, main=251*, sub=15*)
  1: 0x0017 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-48.260*, z=78.102*, y=0.000*, direction=10.3°*
  2: 0x0020 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 30 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    B6 0B 08 80 00 80 09  80 09 80 09 80 09 80 0A   ...............
0030: 80 06 80 06 80 37 0B 80  0C 80 06 80 0D 80 00     .....7......... 
```

#### Opcodes

```
  0: 0x0021 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=8*, head=11*, body=11*, hands=11*, legs=11*, feet=20*, main=0*, sub=0*)
  1: 0x0035 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-58.339*, z=99.044*, y=0.000*, direction=294.7°*
  2: 0x003E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003F   |
| Data Size    | 30 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               B6                 .
0040: 0B 0E 80 0F 80 06 80 10  80 10 80 10 80 0A 80 06  ................
0050: 80 06 80 37 11 80 12 80  13 80 14 80 00           ...7.........   
```

#### Opcodes

```
  0: 0x003F [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=2*, hair=4*, head=0*, body=54*, hands=54*, legs=54*, feet=20*, main=0*, sub=0*)
  1: 0x0053 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=28.754*, z=-126.888*, y=-6.000*, direction=95.7°*
  2: 0x005C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005D   |
| Data Size    | 38 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         37 15 80               7..
0060: 16 80 06 80 17 80 B6 0B  18 80 00 80 02 80 02 80  ................
0070: 02 80 02 80 02 80 03 80  06 80 22 00 2F 00 F8 FF  .........."./...
0080: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x005D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-103.616*, z=-21.440*, y=0.000*, direction=56.9°*
  1: 0x0066 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=8*, head=15*, body=15*, hands=15*, legs=15*, feet=15*, main=251*, sub=0*)
  2: 0x007A [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  3: 0x007C [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  4: 0x0082 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0083  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:          22 01 2F 01 06  21 03 01 00                 "./..!...    
```

#### Opcodes

```
  0: 0x0083 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0085 [0x2F] Achetragond (ID: 16982278/0x01032106)->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x008B [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                      32 19 80 1F              2...
0090: 00 1A 80 1B 80 06 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x008C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x008F [0x1F] MOVE_ENTITY: EventEntity moves to X=-96.766*, Z=-20.917*, Y=0.000*
  2: 0x0097 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0099 [0x00] END_REQSTACK()
```
