# 17350989 - kagami_test

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ghelsba Outpost (ID: 140) |
| Block Size       | 196 bytes                 |
| Total Events     | 5                         |
| References Count | 15                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     32 |              5 |
| [32000](#event-32000)    | 0x0021       |     32 |              5 |
| [32004](#event-32004)    | 0x0041       |     12 |              3 |
| [65535.2](#event-655352) | 0x004D       |     21 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFD10E1  |  4294775009 |
|       1 | 0xA904      |       43268 |
|       2 | 0xFFFFD508  |  4294956296 |
|       3 | 0x0233      |         563 |
|       4 | 0x00F0      |         240 |
|       5 | 0x0003      |           3 |
|       6 | 0x0000      |           0 |
|       7 | 0xFFFD14C9  |  4294776009 |
|       8 | 0xFFFFD40E  |  4294956046 |
|       9 | 0x0078      |         120 |
|      10 | 0xFFFD099A  |  4294773146 |
|      11 | 0x9DD0      |       40400 |
|      12 | 0xFFFFD8F0  |  4294957296 |
|      13 | 0x0E8E      |        3726 |
|      14 | 0x003C      |          60 |

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 32 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    33 01 37 00 80 01 80  02 80 03 80 1C 04 80 62   3.7...........b
0010: 05 80 4D C1 08 01 4D C1  08 01 6D 61 69 6E 06 80  ..M...M...main..
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0003 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-192.287*, z=43.268*, y=-11.000*, direction=49.5°*
  2: 0x000C [0x1C] WAIT(240* ticks)
  3: 0x000F [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [kagami_test (ID: 17350989/0x0108C14D), kagami_test (ID: 17350989/0x0108C14D)], work=[3*, 0*]
  4: 0x0020 [0x00] END_REQSTACK()
```

### Event 32000

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 32 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    33 01 37 07 80 01 80  08 80 03 80 1C 09 80 62   3.7...........b
0030: 05 80 4D C1 08 01 4D C1  08 01 6D 61 69 6E 06 80  ..M...M...main..
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x0021 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0023 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-191.287*, z=43.268*, y=-11.250*, direction=49.5°*
  2: 0x002C [0x1C] WAIT(120* ticks)
  3: 0x002F [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [kagami_test (ID: 17350989/0x0108C14D), kagami_test (ID: 17350989/0x0108C14D)], work=[3*, 0*]
  4: 0x0040 [0x00] END_REQSTACK()
```

### Event 32004

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0041   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:    33 01 37 0A 80 0B 80  0C 80 0D 80 00            3.7.........   
```

#### Opcodes

```
  0: 0x0041 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0043 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-194.150*, z=40.400*, y=-10.000*, direction=327.5°*
  2: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 21 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         1C 0E 80               ...
0050: 62 05 80 4D C1 08 01 4D  C1 08 01 6D 61 69 6E 06  b..M...M...main.
0060: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x004D [0x1C] WAIT(60* ticks)
  1: 0x0050 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [kagami_test (ID: 17350989/0x0108C14D), kagami_test (ID: 17350989/0x0108C14D)], work=[3*, 0*]
  2: 0x0061 [0x00] END_REQSTACK()
```
