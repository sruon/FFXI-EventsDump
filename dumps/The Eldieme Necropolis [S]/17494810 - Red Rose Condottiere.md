# 17494810 - Red Rose Condottiere

## Common Data

| Field            | Value                                |
|------------------|--------------------------------------|
| Zone             | The Eldieme Necropolis [S] (ID: 175) |
| Block Size       | 164 bytes                            |
| Total Events     | 4                                    |
| References Count | 16                                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [49](#event-49)          | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     15 |              5 |
| [65535.2](#event-655352) | 0x0017       |     45 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0xFFFC73C4  |  4294734788 |
|       2 | 0x1B410     |      111632 |
|       3 | 0x045F      |        1119 |
|       4 | 0xFFFC5778  |  4294727544 |
|       5 | 0x1CE87     |      118407 |
|       6 | 0x03E7      |         999 |
|       7 | 0xFFFC18BA  |  4294711482 |
|       8 | 0x21E02     |      138754 |
|       9 | 0x001D      |          29 |
|      10 | 0xFFFC0E57  |  4294708823 |
|      11 | 0x23737     |      145207 |
|      12 | 0xFFFFFFA3  |  4294967203 |
|      13 | 0xFFFC0C7D  |  4294708349 |
|      14 | 0x25FA9     |      155561 |
|      15 | 0x0049      |          73 |

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

### Event 49

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          32 00 80 1F 00 01 80 02          2.......
0010: 80 03 80 1F 01 6F 00                              .....o.         
```

#### Opcodes

```
  0: 0x0008 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x000B [0x1F] MOVE_ENTITY: EventEntity moves to X=-232.508*, Z=111.632*, Y=1.119*
  2: 0x0013 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0015 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 45 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      32  00 80 1F 00 04 80 05 80         2........
0020: 06 80 1F 01 1F 00 07 80  08 80 09 80 1F 01 1F 00  ................
0030: 0A 80 0B 80 0C 80 1F 01  1F 00 0D 80 0E 80 0F 80  ................
0040: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x0017 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x001A [0x1F] MOVE_ENTITY: EventEntity moves to X=-239.752*, Z=118.407*, Y=0.999*
  2: 0x0022 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0024 [0x1F] MOVE_ENTITY: EventEntity moves to X=-255.814*, Z=138.754*, Y=0.029*
  4: 0x002C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x002E [0x1F] MOVE_ENTITY: EventEntity moves to X=-258.473*, Z=145.207*, Y=-0.093*
  6: 0x0036 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0038 [0x1F] MOVE_ENTITY: EventEntity moves to X=-258.947*, Z=155.561*, Y=0.073*
  8: 0x0040 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x0042 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 10: 0x0043 [0x00] END_REQSTACK()
```
