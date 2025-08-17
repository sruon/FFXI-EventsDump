# 17171152 - Pattna-Ottna

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Fort Karugo-Narugo [S] (ID: 96) |
| Block Size       | 144 bytes                       |
| Total Events     | 7                               |
| References Count | 11                              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [106](#event-106)        | 0x0001       |      1 |              1 |
| [111](#event-111)        | 0x0002       |      1 |              1 |
| [105](#event-105)        | 0x0003       |      1 |              1 |
| [65535.1](#event-655351) | 0x0004       |     20 |              6 |
| [65535.2](#event-655352) | 0x0018       |     12 |              3 |
| [65535.3](#event-655353) | 0x0024       |     19 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0xFFFF2C4E  |  4294913102 |
|       2 | 0xFFFFFFE8  |  4294967272 |
|       3 | 0xFFFED764  |  4294891364 |
|       4 | 0x1F0C3     |      127171 |
|       5 | 0x0C4E      |        3150 |
|       6 | 0xFFFF3E04  |  4294917636 |
|       7 | 0x0013      |          19 |
|       8 | 0x20148     |      131400 |
|       9 | 0x13A5      |        5029 |
|      10 | 0xFFFF3D42  |  4294917442 |

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

### Event 106

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

### Event 111

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

### Event 105

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
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             32 00 80 1F  00 01 80 02 80 03 80 1F      2...........
0010: 01 6F 1E F8 02 06 01 00                           .o......        
```

#### Opcodes

```
  0: 0x0004 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0007 [0x1F] MOVE_ENTITY: EventEntity moves to X=-54.194*, Z=-0.024*, Y=-75.932*
  2: 0x000F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0011 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0012 [0x1E] EventEntity looks at Robel-Akbel (ID: 17171192/0x010602F8) and starts talking
  5: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          33 01 37 04 80 05 80 06          3.7.....
0020: 80 07 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0018 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x001A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=127.171*, z=3.150*, y=-49.660*, direction=1.7°*
  2: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             32 00 80 5A  00 08 80 09 80 0A 80 5A      2..Z.......Z
0030: 01 1E 22 03 06 01 00                              .."....         
```

#### Opcodes

```
  0: 0x0024 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0027 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=131.400*, Z=5.029*, Y=-49.854*
  2: 0x002F [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x0031 [0x1E] EventEntity looks at Joseaneaut (ID: 17171234/0x01060322) and starts talking
  4: 0x0036 [0x00] END_REQSTACK()
```
