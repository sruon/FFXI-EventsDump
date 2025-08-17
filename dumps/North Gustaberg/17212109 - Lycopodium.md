# 17212109 - Lycopodium

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | North Gustaberg (ID: 106) |
| Block Size       | 44 bytes                  |
| Total Events     | 3                         |
| References Count | 0                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [264](#event-264)     | 0x0001       |      7 |              2 |
| [265](#event-265)     | 0x0008       |      7 |              2 |

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

### Event 264

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4E 00 F8 FF FF 7F 00                            N......        
```

#### Opcodes

```
  0: 0x0001 [0x4E] SET_ENTITY_HIDE_FLAG: Show EventEntity
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 265

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          4E 00 F8 FF FF 7F 00             N...... 
```

#### Opcodes

```
  0: 0x0008 [0x4E] SET_ENTITY_HIDE_FLAG: Show EventEntity
  1: 0x000E [0x00] END_REQSTACK()
```
