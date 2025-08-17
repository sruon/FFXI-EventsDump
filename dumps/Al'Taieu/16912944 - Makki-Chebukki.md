# 16912944 - Makki-Chebukki

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Al'Taieu (ID: 33) |
| Block Size       | 164 bytes         |
| Total Events     | 5                 |
| References Count | 16                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      7 |              2 |
| [161](#event-161)        | 0x0007       |     10 |              2 |
| [65535.1](#event-655351) | 0x0011       |     18 |              6 |
| [65535.2](#event-655352) | 0x0023       |     19 |              5 |
| [163](#event-163)        | 0x0036       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00B6      |         182 |
|       1 | 0xFFF4EF7B  |  4294242171 |
|       2 | 0xFFFFF153  |  4294963539 |
|       3 | 0x043D      |        1085 |
|       4 | 0x0028      |          40 |
|       5 | 0x0066      |         102 |
|       6 | 0xFFF4D253  |  4294234707 |
|       7 | 0x0005      |           5 |
|       8 | 0x001A      |          26 |
|       9 | 0xFFFFFEF4  |  4294967028 |
|      10 | 0xFFF50701  |  4294248193 |
|      11 | 0xFFFFF428  |  4294964264 |
|      12 | 0xFFF59928  |  4294285608 |
|      13 | 0xFFFC9E56  |  4294745686 |
|      14 | 0xFFFFF059  |  4294963289 |
|      15 | 0x0778      |        1912 |

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

### Event 161

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
  0: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.182*, z=-725.125*, y=-3.757*, direction=95.4°*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 04 80 1F 00 05 80  06 80 02 80 1F 01 6F 1C   2............o.
0020: 07 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.102*, Z=-732.589*, Y=-3.757*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x001F [0x1C] WAIT(5* ticks)
  5: 0x0022 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          7B F8 FF FF 7F  32 08 80 1F 00 09 80 0A     {....2.......
0030: 80 0B 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0023 [0x7B] EventEntity stops talking
  1: 0x0028 [0x32] ExtData[1]->MainSpeed = 26* * 0.1
  2: 0x002B [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.268*, Z=-719.103*, Y=-3.032*
  3: 0x0033 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0035 [0x00] END_REQSTACK()
```

### Event 163

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0036   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   37 0C  80 0D 80 0E 80 0F 80 00        7.........
```

#### Opcodes

```
  0: 0x0036 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-681.688*, z=-221.610*, y=-4.007*, direction=168.0°*
  1: 0x003F [0x00] END_REQSTACK()
```
