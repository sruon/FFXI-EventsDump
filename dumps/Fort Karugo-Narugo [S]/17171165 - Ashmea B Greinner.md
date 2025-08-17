# 17171165 - Ashmea B Greinner

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Fort Karugo-Narugo [S] (ID: 96) |
| Block Size       | 168 bytes                       |
| Total Events     | 5                               |
| References Count | 14                              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [111](#event-111)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     30 |              4 |
| [65535.2](#event-655352) | 0x0020       |     15 |              5 |
| [65535.3](#event-655353) | 0x002F       |     27 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x0050      |          80 |
|       3 | 0x27814     |      161812 |
|       4 | 0xC391      |       50065 |
|       5 | 0xFFFF59C3  |  4294924739 |
|       6 | 0x26B71     |      158577 |
|       7 | 0xC453      |       50259 |
|       8 | 0xFFFF5933  |  4294924595 |
|       9 | 0x04E1      |        1249 |
|      10 | 0x25A27     |      154151 |
|      11 | 0x8EB1      |       36529 |
|      12 | 0xFFFF525B  |  4294922843 |
|      13 | 0x04E2      |        1250 |

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

### Event 111

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
| Data Size    | 30 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       7E 06 F8 FF FF 7F  00 80 01 80 00 80 00 80    ~.............
0010: 00 80 00 80 7E 04 F8 FF  FF 7F 80 F8 FF FF 7F 00  ....~...........
```

#### Opcodes

```
  0: 0x0002 [0x7E] CHOCOBO_MOUNT: Mode 6 (custom mount) on EventEntity
  1: 0x0014 [0x7E] CHOCOBO_MOUNT: Mode 4 on EventEntity
  2: 0x001A [0x80] LOAD_WAIT(entity=EventEntity)
  3: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 32 02 80 1F 00 03 80 04  80 05 80 1F 01 6F 00     2............o. 
```

#### Opcodes

```
  0: 0x0020 [0x32] ExtData[1]->MainSpeed = 80* * 0.1
  1: 0x0023 [0x1F] MOVE_ENTITY: EventEntity moves to X=161.812*, Z=50.065*, Y=-42.557*
  2: 0x002B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 27 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               37                 7
0030: 06 80 07 80 08 80 09 80  32 02 80 1F 00 0A 80 0B  ........2.......
0040: 80 0C 80 1F 01 6F 39 0D  80 00                    .....o9...      
```

#### Opcodes

```
  0: 0x002F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=158.577*, z=50.259*, y=-42.701*, direction=109.8°*
  1: 0x0038 [0x32] ExtData[1]->MainSpeed = 80* * 0.1
  2: 0x003B [0x1F] MOVE_ENTITY: EventEntity moves to X=154.151*, Z=36.529*, Y=-44.453*
  3: 0x0043 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0045 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0046 [0x39] SET_ENTITY_DIRECTION(direction=6.9°*)
  6: 0x0049 [0x00] END_REQSTACK()
```
