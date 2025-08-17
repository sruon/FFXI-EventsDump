# 17776789 - Pheauclemand

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 284 bytes             |
| Total Events     | 12                    |
| References Count | 21                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [10060](#event-10060)    | 0x0001       |      1 |              1 |
| [10205](#event-10205)    | 0x0002       |      1 |              1 |
| [10062](#event-10062)    | 0x0003       |      1 |              1 |
| [10207](#event-10207)    | 0x0004       |      1 |              1 |
| [65535.1](#event-655351) | 0x0005       |     23 |              5 |
| [65535.2](#event-655352) | 0x001C       |     14 |              4 |
| [65535.3](#event-655353) | 0x002A       |     21 |              5 |
| [65535.4](#event-655354) | 0x003F       |     15 |              5 |
| [65535.5](#event-655355) | 0x004E       |     13 |              3 |
| [65535.6](#event-655356) | 0x005B       |     17 |              4 |
| [65535.7](#event-655357) | 0x006C       |     27 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFF3100  |  4294914304 |
|       1 | 0xB244      |       45636 |
|       2 | 0xFFFFFF39  |  4294967097 |
|       3 | 0x05F0      |        1520 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFF2BEA  |  4294913002 |
|       6 | 0xE06C      |       57452 |
|       7 | 0x0000      |           0 |
|       8 | 0xFFFF4289  |  4294918793 |
|       9 | 0x0831      |        2097 |
|      10 | 0xFFFFFE0D  |  4294966797 |
|      11 | 0xFFFF53D1  |  4294923217 |
|      12 | 0xFFFFFB8C  |  4294966156 |
|      13 | 0xFFFF45CD  |  4294919629 |
|      14 | 0x0010      |          16 |
|      15 | 0x003C      |          60 |
|      16 | 0xFFFF40CE  |  4294918350 |
|      17 | 0x0CE1      |        3297 |
|      18 | 0xFFFF2750  |  4294911824 |
|      19 | 0x0D24      |        3364 |
|      20 | 0xFFFFFE0C  |  4294966796 |

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

### Event 10060

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

### Event 10205

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

### Event 10062

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

### Event 10207

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0004  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             00                                        .           
```

#### Opcodes

```
  0: 0x0004 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0005   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                2F 00 F8  FF FF 7F 37 00 80 01 80       /.....7....
0010: 02 80 03 80 22 00 80 F8  FF FF 7F 00              ....".......    
```

#### Opcodes

```
  0: 0x0005 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x000B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-52.992*, z=45.636*, y=-0.199*, direction=133.6°*
  2: 0x0014 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  3: 0x0016 [0x80] LOAD_WAIT(entity=EventEntity)
  4: 0x001B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      32 04 80 1F              2...
0020: 00 05 80 06 80 07 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x001C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001F [0x1F] MOVE_ENTITY: EventEntity moves to X=-54.294*, Z=57.452*, Y=0.000*
  2: 0x0027 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 21 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                2F 00 F8 FF FF 7F            /.....
0030: 36 08 80 09 80 0A 80 22  00 80 F8 FF FF 7F 00     6......"....... 
```

#### Opcodes

```
  0: 0x002A [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x0030 [0x36] SET_ENTITY_EVENT_POSITION(pos_x=-48.503*, pos_z=2.097*, pos_y=-0.499*)
  2: 0x0037 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  3: 0x0039 [0x80] LOAD_WAIT(entity=EventEntity)
  4: 0x003E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003F   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               32                 2
0040: 04 80 1F 00 0B 80 0C 80  0A 80 1F 01 6F 00        ............o.  
```

#### Opcodes

```
  0: 0x003F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0042 [0x1F] MOVE_ENTITY: EventEntity moves to X=-44.079*, Z=-1.140*, Y=-0.499*
  2: 0x004A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            36 0D                6.
0050: 80 0E 80 0A 80 1E F0 FF  FF 7F 00                 ...........     
```

#### Opcodes

```
  0: 0x004E [0x36] SET_ENTITY_EVENT_POSITION(pos_x=-47.667*, pos_z=0.016*, pos_y=-0.499*)
  1: 0x0055 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 17 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   1C 0F 80 79 00             ...y.
0060: 95 40 0F 01 8F 40 0F 01  1C 0F 80 00              .@...@......    
```

#### Opcodes

```
  0: 0x005B [0x1C] WAIT(60* ticks)
  1: 0x005E [0x79] Pheauclemand (ID: 17776789/0x010F4095) looks at Unnamed NPC (ID: 17776783/0x010F408F) (Basic look)
  2: 0x0068 [0x1C] WAIT(60* ticks)
  3: 0x006B [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006C   |
| Data Size    | 27 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      32 04 80 1F              2...
0070: 00 10 80 11 80 0A 80 1F  01 1F 00 12 80 13 80 14  ................
0080: 80 1F 01 6F 22 01 00                              ...o"..         
```

#### Opcodes

```
  0: 0x006C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x006F [0x1F] MOVE_ENTITY: EventEntity moves to X=-48.946*, Z=3.297*, Y=-0.499*
  2: 0x0077 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0079 [0x1F] MOVE_ENTITY: EventEntity moves to X=-55.472*, Z=3.364*, Y=-0.500*
  4: 0x0081 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0083 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0084 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  7: 0x0086 [0x00] END_REQSTACK()
```
