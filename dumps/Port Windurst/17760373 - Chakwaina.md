# 17760373 - Chakwaina

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Port Windurst (ID: 240) |
| Block Size       | 68 bytes                |
| Total Events     | 4                       |
| References Count | 3                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |      1 |              1 |
| [65535.2](#event-655352) | 0x0002       |      9 |              3 |
| [350](#event-350)        | 0x000B       |     12 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x100C      |        4108 |
|       2 | 0x100D      |        4109 |

## String References

- **4108**: So this is one of the wooden puppet-monsters the Tarutaru created, eh?
- **4109**: Why, it looks a lot cuter than I had expected. Let's see if it will eat these nuts. Here boy, eat! C'mon eat it, boy!

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

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       5E 69 64 6C 30 1C  00 80 00                   ^idl0....     
```

#### Opcodes

```
  0: 0x0002 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0007 [0x1C] WAIT(30* ticks)
  2: 0x000A [0x00] END_REQSTACK()
```

### Event 350

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 12 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   1D 01 80 23 1D             ...#.
0010: 02 80 23 20 00 21 00                              ..# .!.         
```

#### Opcodes

```
  0: 0x000B [0x1D] PRINT_EVENT_MESSAGE(message_id=4108*)
    → "So this is one of the wooden puppet-monsters the Tarutaru created, eh?"
  1: 0x000E [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x000F [0x1D] PRINT_EVENT_MESSAGE(message_id=4109*)
    → "Why, it looks a lot cuter than I had expected. Let's see if it will eat these nuts. Here boy, eat! C'mon eat it, boy!"
  3: 0x0012 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0013 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  5: 0x0015 [0x21] END_EVENT
  6: 0x0016 [0x00] END_REQSTACK()
```
