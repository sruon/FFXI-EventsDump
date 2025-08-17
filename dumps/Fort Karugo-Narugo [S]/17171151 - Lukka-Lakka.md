# 17171151 - Lukka-Lakka

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Fort Karugo-Narugo [S] (ID: 96) |
| Block Size       | 128 bytes                       |
| Total Events     | 5                               |
| References Count | 9                               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [111](#event-111)        | 0x0001       |      1 |              1 |
| [105](#event-105)        | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     26 |              3 |
| [65535.2](#event-655352) | 0x001D       |     26 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0003      |           3 |
|       1 | 0x0009      |           9 |
|       2 | 0x0000      |           0 |
|       3 | 0x000C      |          12 |
|       4 | 0x00FD      |         253 |
|       5 | 0x0005      |           5 |
|       6 | 0x000B      |          11 |
|       7 | 0x006D      |         109 |
|       8 | 0x0118      |         280 |

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

### Event 105

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 26 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          B6 0B 00 80 01  80 02 80 03 80 03 80 03     .............
0010: 80 03 80 04 80 02 80 80  F8 FF FF 7F 00           .............   
```

#### Opcodes

```
  0: 0x0003 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=9*, head=0*, body=12*, hands=12*, legs=12*, feet=12*, main=253*, sub=0*)
  1: 0x0017 [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001D   |
| Data Size    | 26 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         B6 0B 05               ...
0020: 80 06 80 07 80 07 80 07  80 07 80 07 80 08 80 02  ................
0030: 80 80 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x001D [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=5*, hair=11*, head=109*, body=109*, hands=109*, legs=109*, feet=109*, main=280*, sub=0*)
  1: 0x0031 [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x0036 [0x00] END_REQSTACK()
```
