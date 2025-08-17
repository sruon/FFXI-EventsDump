# 16863327 - Ealdnarche

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Spire of Mea (ID: 21) |
| Block Size       | 100 bytes             |
| Total Events     | 5                     |
| References Count | 4                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     15 |              4 |
| [23](#event-23)          | 0x0010       |      7 |              2 |
| [65535.2](#event-655352) | 0x0017       |     10 |              2 |
| [32001](#event-32001)    | 0x0021       |     15 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFF95110  |  4294529296 |
|       1 | 0x61A80     |      400000 |
|       2 | 0xFFFFB565  |  4294948197 |
|       3 | 0x0032      |          50 |

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
| Data Size    | 15 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 94  01 F8 FF FF 7F A4 01 00   ...............
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000D [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  3: 0x000F [0x00] END_REQSTACK()
```

### Event 23

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0010  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0010 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      37  00 80 01 80 02 80 03 80         7........
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0017 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-438.000*, z=400.000*, y=-19.099*, direction=4.4°*
  1: 0x0020 [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 15 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    92 01 F8 FF FF 7F 94  01 F8 FF FF 7F A4 01 00   ...............
```

#### Opcodes

```
  0: 0x0021 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0027 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x002D [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  3: 0x002F [0x00] END_REQSTACK()
```
