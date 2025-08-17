# 16912949 - Louverance

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Al'Taieu (ID: 33) |
| Block Size       | 152 bytes         |
| Total Events     | 5                 |
| References Count | 10                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      7 |              2 |
| [164](#event-164)        | 0x0007       |     10 |              2 |
| [65535.1](#event-655351) | 0x0011       |     15 |              5 |
| [65535.2](#event-655352) | 0x0020       |     17 |              6 |
| [65535.3](#event-655353) | 0x0031       |     25 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x05DC      |        1500 |
|       1 | 0xFFF8D339  |  4294497081 |
|       2 | 0xFFFFD8F1  |  4294957297 |
|       3 | 0x0A2B      |        2603 |
|       4 | 0x000D      |          13 |
|       5 | 0x04B0      |        1200 |
|       6 | 0xFFF8EA6C  |  4294503020 |
|       7 | 0x0014      |          20 |
|       8 | 0xFFF8F784  |  4294506372 |
|       9 | 0xFFF8F23C  |  4294505020 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0000 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x00] END_REQSTACK()
```

### Event 164

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0007   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      37  00 80 01 80 02 80 03 80         7........
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=1.500*, z=-470.215*, y=-9.999*, direction=228.8°*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 04 80 1F 00 05 80  06 80 02 80 1F 01 6F 00   2............o.
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.200*, Z=-464.276*, Y=-9.999*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 17 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 33 01 32 04 80 1F 00 07  80 08 80 02 80 1F 01 6F  3.2............o
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0020 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0022 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0025 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.020*, Z=-460.924*, Y=-9.999*
  3: 0x002D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x002F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0030 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0031   |
| Data Size    | 25 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    32 04 80 1F 00 05 80  09 80 02 80 1F 01 1F 00   2..............
0040: 05 80 01 80 02 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x0031 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0034 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.200*, Z=-462.276*, Y=-9.999*
  2: 0x003C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003E [0x1F] MOVE_ENTITY: EventEntity moves to X=1.200*, Z=-470.215*, Y=-9.999*
  4: 0x0046 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0048 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0049 [0x00] END_REQSTACK()
```
