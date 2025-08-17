# 16883768 - Mildaurion

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 72 bytes                    |
| Total Events     | 3                           |
| References Count | 4                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [104](#event-104)        | 0x0001       |     15 |              4 |
| [65535.1](#event-655351) | 0x0010       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x4010      |       16400 |
|       1 | 0x0190      |         400 |
|       2 | 0x07CF      |        1999 |
|       3 | 0x0762      |        1890 |

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

### Event 104

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 37 00 80 01 80 02 80 03  80 00                    7.........      
```

#### Opcodes

```
  0: 0x0010 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=16.400*, z=0.400*, y=1.999*, direction=166.1°*
  1: 0x0019 [0x00] END_REQSTACK()
```
