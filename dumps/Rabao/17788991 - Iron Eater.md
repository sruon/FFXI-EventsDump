# 17788991 - Iron Eater

## Common Data

| Field            | Value           |
|------------------|-----------------|
| Zone             | Rabao (ID: 247) |
| Block Size       | 104 bytes       |
| Total Events     | 4               |
| References Count | 8               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [102](#event-102)        | 0x0001       |      1 |              1 |
| [104](#event-104)        | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     35 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x32E8      |       13032 |
|       2 | 0x14145     |       82245 |
|       3 | 0x1F40      |        8000 |
|       4 | 0x0C95      |        3221 |
|       5 | 0x27F3      |       10227 |
|       6 | 0x14001     |       81921 |
|       7 | 0x1F3F      |        7999 |

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

### Event 102

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

### Event 104

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
| Data Size    | 35 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          22 00 79 00 F8  FF FF 7F 3D 70 0F 01 32     ".y.....=p..2
0010: 00 80 37 01 80 02 80 03  80 04 80 1F 00 05 80 06  ..7.............
0020: 80 07 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0003 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0005 [0x79] EventEntity looks at Dancing Wolf (ID: 17788989/0x010F703D) (Basic look)
  2: 0x000F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x0012 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=13.032*, z=82.245*, y=8.000*, direction=283.1°*
  4: 0x001B [0x1F] MOVE_ENTITY: EventEntity moves to X=10.227*, Z=81.921*, Y=7.999*
  5: 0x0023 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0025 [0x00] END_REQSTACK()
```
