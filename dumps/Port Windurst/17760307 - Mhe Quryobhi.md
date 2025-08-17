# 17760307 - Mhe Quryobhi

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Port Windurst (ID: 240) |
| Block Size       | 56 bytes                |
| Total Events     | 3                       |
| References Count | 2                       |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [206](#event-206)     | 0x0001       |      8 |              5 |
| [316](#event-316)     | 0x0009       |      8 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0E16      |        3606 |
|       1 | 0x0F61      |        3937 |

## String References

- **3606**: Hee-hee-hee... When you scatterrr the bait like this, the fish all gatherrr togetherrr, and theirrr scales shine in the light. It's rrreal purrretty...
- **3937**: Huh? Burrrnite shell? I've neverrr hearrrd of such a shell, neitherrr in the sea orrr on the land!

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

### Event 206

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 8 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 20 00 21  00                        ...# .!.       
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=3606*)
    → "Hee-hee-hee... When you scatterrr the bait like this, the fish all gatherrr togetherrr, and theirrr scales shine in the light. It's rrreal purrretty..."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  3: 0x0007 [0x21] END_EVENT
  4: 0x0008 [0x00] END_REQSTACK()
```

### Event 316

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0009  |
| Data Size    | 8 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                             1D 01 80 23 20 00 21           ...# .!
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=3937*)
    → "Huh? Burrrnite shell? I've neverrr hearrrd of such a shell, neitherrr in the sea orrr on the land!"
  1: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x000D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  3: 0x000F [0x21] END_EVENT
  4: 0x0010 [0x00] END_REQSTACK()
```
