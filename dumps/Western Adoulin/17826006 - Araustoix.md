# 17826006 - Araustoix

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Western Adoulin (ID: 256) |
| Block Size       | 272 bytes                 |
| Total Events     | 7                         |
| References Count | 25                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [181](#event-181)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     34 |              8 |
| [190](#event-190)        | 0x0024       |     21 |              2 |
| [65535.2](#event-655352) | 0x0039       |     22 |              6 |
| [65535.3](#event-655353) | 0x004F       |     27 |              7 |
| [65535.4](#event-655354) | 0x006A       |     21 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFD9568  |  4294808936 |
|       2 | 0xFFFF9D85  |  4294942085 |
|       3 | 0x0A8B      |        2699 |
|       4 | 0xFFFD84F5  |  4294804725 |
|       5 | 0xFFFF9DA0  |  4294942112 |
|       6 | 0xFFFD73AC  |  4294800300 |
|       7 | 0xFFFF9D99  |  4294942105 |
|       8 | 0x0DEC      |        3564 |
|       9 | 0x0008      |           8 |
|      10 | 0x0002      |           2 |
|      11 | 0x0000      |           0 |
|      12 | 0x0017      |          23 |
|      13 | 0xFFFF23E0  |  4294910944 |
|      14 | 0xFFFFE531  |  4294960433 |
|      15 | 0xFFFFFE0C  |  4294966796 |
|      16 | 0x001E      |          30 |
|      17 | 0xFFFF191E  |  4294908190 |
|      18 | 0xFFFFF7D5  |  4294965205 |
|      19 | 0xFFFF2A00  |  4294912512 |
|      20 | 0x0275      |         629 |
|      21 | 0x0003      |           3 |
|      22 | 0x0009      |           9 |
|      23 | 0x0014      |          20 |
|      24 | 0x008F      |         143 |

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

### Event 181

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
| Data Size    | 34 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 1F    2.............
0010: 00 04 80 05 80 03 80 1F  01 1F 00 06 80 07 80 08  ................
0020: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=-158.360*, Z=-25.211*, Y=2.699*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=-162.571*, Z=-25.184*, Y=2.699*
  4: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0019 [0x1F] MOVE_ENTITY: EventEntity moves to X=-166.996*, Z=-25.191*, Y=3.564*
  6: 0x0021 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0023 [0x00] END_REQSTACK()
```

### Event 190

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             B6 0B 09 80  0A 80 0B 80 0C 80 0B 80      ............
0030: 0A 80 0A 80 0B 80 0B 80  00                       .........       
```

#### Opcodes

```
  0: 0x0024 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=8*, hair=2*, head=0*, body=23*, hands=0*, legs=2*, feet=2*, main=0*, sub=0*)
  1: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             32 00 80 1F 00 0D 80           2......
0040: 0E 80 0F 80 1F 01 1E CD  00 10 01 1C 10 80 00     ............... 
```

#### Opcodes

```
  0: 0x0039 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003C [0x1F] MOVE_ENTITY: EventEntity moves to X=-56.352*, Z=-6.863*, Y=-0.500*
  2: 0x0044 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0046 [0x1E] EventEntity looks at Ilney (ID: 17825997/0x011000CD) and starts talking
  4: 0x004B [0x1C] WAIT(30* ticks)
  5: 0x004E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004F   |
| Data Size    | 27 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               32                 2
0050: 00 80 1F 00 11 80 12 80  0F 80 1F 01 1C 10 80 1F  ................
0060: 00 13 80 14 80 0F 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x004F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0052 [0x1F] MOVE_ENTITY: EventEntity moves to X=-59.106*, Z=-2.091*, Y=-0.500*
  2: 0x005A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005C [0x1C] WAIT(30* ticks)
  4: 0x005F [0x1F] MOVE_ENTITY: EventEntity moves to X=-54.784*, Z=0.629*, Y=-0.500*
  5: 0x0067 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0069 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006A   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                B6 0B 15 80 16 80            ......
0070: 17 80 18 80 0C 80 18 80  18 80 0B 80 0B 80 00     ............... 
```

#### Opcodes

```
  0: 0x006A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=9*, head=20*, body=143*, hands=23*, legs=143*, feet=143*, main=0*, sub=0*)
  1: 0x007E [0x00] END_REQSTACK()
```
