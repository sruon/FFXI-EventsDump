# 17752325 - Kogri-Nargri

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 116 bytes                 |
| Total Events     | 5                         |
| References Count | 10                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [905](#event-905)        | 0x0001       |     15 |              7 |
| [906](#event-906)        | 0x0010       |      1 |              1 |
| [65535.1](#event-655351) | 0x0011       |     10 |              2 |
| [65535.2](#event-655352) | 0x001B       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2CED      |       11501 |
|       1 | 0x2CEE      |       11502 |
|       2 | 0xFFFEED9C  |  4294897052 |
|       3 | 0xFFFFEEA9  |  4294962857 |
|       4 | 0xFFFFF128  |  4294963496 |
|       5 | 0x08BD      |        2237 |
|       6 | 0xFFFEF2A1  |  4294898337 |
|       7 | 0xFFFFDFC2  |  4294959042 |
|       8 | 0xFFFFF254  |  4294963796 |
|       9 | 0x0991      |        2449 |

## String References

- **11501**: Nice taru meet you! My name is Kogri-Nargri. I just started working for Chamama!
- **11502**: 20 years ago, there was a terrible fire that burned the Rarab Tail's roof right off. I'm glad I wasn'taru around when that happened!

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

### Event 905

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 1D 01 80 23 21 00   ........#...#!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=11501*)
    → "Nice taru meet you! My name is Kogri-Nargri. I just started working for Chamama!"
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=11502*)
    → "20 years ago, there was a terrible fire that burned the Rarab Tail's roof right off. I'm glad I wasn'taru around when that happened!"
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x21] END_EVENT
  6: 0x000F [0x00] END_REQSTACK()
```

### Event 906

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0010  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    37 02 80 03 80 04 80  05 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0011 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-70.244*, z=-4.439*, y=-3.800*, direction=196.6°*
  1: 0x001A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   37 06 80 07 80             7....
0020: 08 80 09 80 00                                    .....           
```

#### Opcodes

```
  0: 0x001B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-68.959*, z=-8.254*, y=-3.500*, direction=215.2°*
  1: 0x0024 [0x00] END_REQSTACK()
```
