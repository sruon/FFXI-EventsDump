# 17780991 - Fhelm Jobeizat

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Lower Jeuno (ID: 245) |
| Block Size       | 188 bytes             |
| Total Events     | 7                     |
| References Count | 10                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [20041](#event-20041)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     24 |              6 |
| [20047](#event-20047)    | 0x001A       |      1 |              1 |
| [65535.2](#event-655352) | 0x001B       |     42 |             10 |
| [65535.3](#event-655353) | 0x0045       |     13 |              3 |
| [65535.4](#event-655354) | 0x0052       |     22 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0xFFFF586D  |  4294924397 |
|       2 | 0xFFFF39BA  |  4294916538 |
|       3 | 0x0000      |           0 |
|       4 | 0xFFFF5DD0  |  4294925776 |
|       5 | 0xFFFF4106  |  4294918406 |
|       6 | 0xFFFF5439  |  4294923321 |
|       7 | 0xFFFF3A10  |  4294916624 |
|       8 | 0x0008      |           8 |
|       9 | 0x000C      |          12 |

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

### Event 20041

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
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 1F    2.............
0010: 00 04 80 05 80 03 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=-42.899*, Z=-50.758*, Y=0.000*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=-41.520*, Z=-48.890*, Y=0.000*
  4: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0019 [0x00] END_REQSTACK()
```

### Event 20047

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                00                           .     
```

#### Opcodes

```
  0: 0x001A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 42 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   32 00 80 1F 00             2....
0020: 06 80 07 80 03 80 1F 01  6F 4A F8 FF FF 7F F6 50  ........oJ.....P
0030: 0F 01 6F 76 F8 FF FF 7F  6E F8 FF FF 7F 08 80 99  ..ov....n.......
0040: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x001B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x001E [0x1F] MOVE_ENTITY: EventEntity moves to X=-43.975*, Z=-50.672*, Y=0.000*
  2: 0x0026 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0028 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0029 [0x4A] EventEntity looks at Nantoto (ID: 17780982/0x010F50F6)
  5: 0x0032 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0033 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  7: 0x0038 [0x6E] EventEntity uses emote 8*
  8: 0x003F [0x99] Wait for EventEntity animation to complete
  9: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                1C 00 80  4A F8 FF FF 7F F0 FF FF       ...J.......
0050: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x0045 [0x1C] WAIT(40* ticks)
  1: 0x0048 [0x4A] EventEntity looks at LocalPlayer
  2: 0x0051 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0052   |
| Data Size    | 22 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       2A 08 F0 FF FF 7F  1C 00 80 6E F8 FF FF 7F    *........n....
0060: 09 80 99 F8 FF FF 7F 00                           ........        
```

#### Opcodes

```
  0: 0x0052 [0x2A] GET_REQ_LEVEL(level=8, entity_id=LocalPlayer)
  1: 0x0058 [0x1C] WAIT(40* ticks)
  2: 0x005B [0x6E] EventEntity uses emote 12*
  3: 0x0062 [0x99] Wait for EventEntity animation to complete
  4: 0x0067 [0x00] END_REQSTACK()
```
