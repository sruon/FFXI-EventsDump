# 17105434 - Raphaillance

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Southern San d'Oria [S] (ID: 80) |
| Block Size       | 160 bytes                        |
| Total Events     | 5                                |
| References Count | 11                               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [55](#event-55)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     33 |             11 |
| [65535.2](#event-655352) | 0x0023       |     22 |              8 |
| [65535.3](#event-655353) | 0x0039       |     20 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0xFFFFFB83  |  4294966147 |
|       2 | 0xB118      |       45336 |
|       3 | 0xFFFFF831  |  4294965297 |
|       4 | 0xFFFFFEB7  |  4294966967 |
|       5 | 0xB011      |       45073 |
|       6 | 0x000D      |          13 |
|       7 | 0xFFFFF821  |  4294965281 |
|       8 | 0xB5F2      |       46578 |
|       9 | 0xFFFFF830  |  4294965296 |
|      10 | 0xD586      |       54662 |

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

### Event 55

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
| Data Size    | 33 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 6F    2............o
0010: 1F 00 04 80 05 80 03 80  1F 01 6F 1E 18 02 05 01  ..........o.....
0020: 6F 70 00                                          op.             
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.149*, Z=45.336*, Y=-1.999*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0010 [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.329*, Z=45.073*, Y=-1.999*
  5: 0x0018 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x001A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x001B [0x1E] EventEntity looks at Halver M Borel (ID: 17105432/0x01050218) and starts talking
  8: 0x0020 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  9: 0x0021 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 10: 0x0022 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 22 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          32 06 80 1F 00  07 80 08 80 09 80 1F 01     2............
0030: 6F 1E 17 02 05 01 6F 70  00                       o.....op.       
```

#### Opcodes

```
  0: 0x0023 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0026 [0x1F] MOVE_ENTITY: EventEntity moves to X=-2.015*, Z=46.578*, Y=-2.000*
  2: 0x002E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0030 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0031 [0x1E] EventEntity looks at Phillieulais S Dieuffon (ID: 17105431/0x01050217) and starts talking
  5: 0x0036 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0037 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             32 06 80 1F 00 01 80           2......
0040: 0A 80 09 80 1F 01 6F 1E  18 02 05 01 00           ......o......   
```

#### Opcodes

```
  0: 0x0039 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003C [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.149*, Z=54.662*, Y=-2.000*
  2: 0x0044 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0046 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0047 [0x1E] EventEntity looks at Halver M Borel (ID: 17105432/0x01050218) and starts talking
  5: 0x004C [0x00] END_REQSTACK()
```
