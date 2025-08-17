# 17347139 - Jagidbod of Clan Reaper

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Horlais Peak (ID: 139) |
| Block Size       | 68 bytes               |
| Total Events     | 3                      |
| References Count | 5                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [32000](#event-32000)    | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |      9 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFF9F265  |  4294570597 |
|       1 | 0xFFFEFF8B  |  4294901643 |
|       2 | 0x171F6     |       94710 |
|       3 | 0x0D3A      |        3386 |
|       4 | 0x029C      |         668 |

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

### Event 32000

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-396.699*, z=-65.653*, y=94.710*, direction=297.6°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000B  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   7B F8 FF FF 7F             {....
0010: 39 04 80 00                                       9...            
```

#### Opcodes

```
  0: 0x000B [0x7B] EventEntity stops talking
  1: 0x0010 [0x39] SET_ENTITY_DIRECTION(direction=3.7°*)
  2: 0x0013 [0x00] END_REQSTACK()
```
