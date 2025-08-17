# 17498653 - Vigsterkr

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Sea Serpent Grotto (ID: 176) |
| Block Size       | 140 bytes                    |
| Total Events     | 4                            |
| References Count | 11                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [18](#event-18)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     14 |              4 |
| [65535.2](#event-655352) | 0x0010       |     46 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x30A70     |      199280 |
|       2 | 0x3FAEE     |      260846 |
|       3 | 0xFFFFD8F0  |  4294957296 |
|       4 | 0x2E578     |      189816 |
|       5 | 0x40A70     |      264816 |
|       6 | 0xFFFFD8B9  |  4294957241 |
|       7 | 0x0464      |        1124 |
|       8 | 0x0001      |           1 |
|       9 | 0x0009      |           9 |
|      10 | 0x001E      |          30 |

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

### Event 18

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
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=199.280*, Z=260.846*, Y=-10.000*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 46 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 37 04 80 05 80 06 80 07  80 4A 1D 02 0B 01 1C 02  7........J......
0020: 0B 01 6F 76 1D 02 0B 01  1C 08 80 66 09 80 1D 02  ..ov.......f....
0030: 0B 01 1D 02 0B 01 73 68  61 30 1C 0A 80 00        ......sha0....  
```

#### Opcodes

```
  0: 0x0010 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=189.816*, z=264.816*, y=-10.055*, direction=98.8°*
  1: 0x0019 [0x4A] Vigsterkr (ID: 17498653/0x010B021D) looks at Gomoya (ID: 17498652/0x010B021C)
  2: 0x0022 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0023 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Vigsterkr (ID: 17498653/0x010B021D) Render.Flags0 and Render.Flags3 conditions are met
  4: 0x0028 [0x1C] WAIT(1* ticks)
  5: 0x002B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [Vigsterkr (ID: 17498653/0x010B021D), Vigsterkr (ID: 17498653/0x010B021D)], work=9*
  6: 0x003A [0x1C] WAIT(30* ticks)
  7: 0x003D [0x00] END_REQSTACK()
```
