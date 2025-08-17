# 17846845 - Lost Article

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Ceizak Battlegrounds (ID: 261) |
| Block Size       | 28 bytes                       |
| Total Events     | 2                              |
| References Count | 0                              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [30011](#event-30011) | 0x0001       |      2 |              2 |

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

### Event 30011

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    21 00                                           !.             
```

#### Opcodes

```
  0: 0x0001 [0x21] END_EVENT
  1: 0x0002 [0x00] END_REQSTACK()
```
