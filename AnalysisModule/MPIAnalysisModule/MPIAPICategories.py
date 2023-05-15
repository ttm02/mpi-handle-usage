import re

is_mpi_builtin = re.compile("MPI_[A-Z_]*")

predefined_mpi_dtype_consants = [
    'MPI_CHAR',
    'MPI_SIGNED_CHAR',
    'MPI_UNSIGNED_CHAR',
    'MPI_BYTE',
    'MPI_WCHAR',
    'MPI_SHORT',
    'MPI_UNSIGNED_SHORT',
    'MPI_INT',
    'MPI_UNSIGNED',
    'MPI_LONG',
    'MPI_UNSIGNED_LONG',
    'MPI_LONG_LONG_INT',
    'MPI_LONG_LONG',
    'MPI_UNSIGNED_LONG_LONG',
    'MPI_FLOAT',
    'MPI_DOUBLE',
    'MPI_LONG_DOUBLE',
    'MPI_C_BOOL',
    'MPI_INT8_T',
    'MPI_INT16_T',
    'MPI_INT32_T'
    'MPI_INT64_T',
    'MPI_UINT8_T',
    'MPI_UINT16_T',
    'MPI_UINT32_T',
    'MPI_UINT64_T',
    'MPI_C_COMPLEX',
    'MPI_C_FLOAT_COMPLEX',
    'MPI_C_DOUBLE_COMPLEX',
    'MPI_C_LONG_DOUBLE_COMPLEX',
    'MPI_BYTE',
    'MPI_PACKED',
    # min/maxloc reduction types
    'MPI_2INT',
    'MPI_FLOAT_INT',
    'MPI_DOUBLE_INT',
    'MPI_LONG_INT',
    'MPI_SHORT_INT',
    'MPI_LONG_DOUBLE_INT',
    # MPI 4
    'MPI_AINT',
    'MPI_COUNT',
    'MPI_OFFSET'
    # Fortran
    'MPI_INTEGER',
    'MPI_REAL',
    'MPI_DOUBLE_PRECISION',
    'MPI_COMPLEX',
    'MPI_LOGICAL',
    'MPI_CHARACTER',
    'MPI_2INTEGER',
    'MPI_2DOUBLE_PRECISION',
    'MPI_2REAL'
]

mpi_optional_predefined_types = [
    # Fortran optionals
    'MPI_DOUBLE_COMPLEX',
    'MPI_INTEGER1',
    'MPI_INTEGER2',
    'MPI_INTEGER4',
    'MPI_INTEGER8',
    'MPI_INTEGER16',
    'MPI_REAL2',
    'MPI_REAL4',
    'MPI_REAL8',
    'MPI_REAL16',
    'MPI_COMPLEX4',
    'MPI_COMPLEX8',
    'MPI_COMPLEX16',
    'MPI_COMPLEX32',
    # CXX bindings
    'MPI_CXX_BOOL',
    'MPI_CXX_FLOAT_COMPLEX',
    'MPI_CXX_DOUBLE_COMPLEX',
    'MPI_CXX_LONG_DOUBLE_COMPLEX',
    # deprecated
    'MPI_UB',
    'MPI_LB'
]

mpi_type_creation_funcs = [
    'MPI_Type_dup',
    'MPI_Type_contiguous',
    'MPI_Type_vector',
    'MPI_Type_create_hvector',
    'MPI_Type_indexed',
    'MPI_Type_create_hindexed',
    'MPI_Type_create_indexed_block',
    'MPI_Type_create_hindexed_block',
    'MPI_Type_create_struct',
    'MPI_Type_create_subarray',
    'MPI_Type_create_darray',
    'MPI_Type_create_resized',
    'MPI_Type_create_f90_complex',
    'MPI_Type_create_f90_integer',
    'MPI_Type_create_f90_real',
    # deprecated
    'MPI_Type_ub',
    'MPI_Type_lb',
    'MPI_Type_extent',
]

predefined_mpi_communicator_consants = [
    'MPI_COMM_WORLD',
    'MPI_COMM_SELF',
    'MPI_COMM_NULL'
]

mpi_comm_creator_funcs = [
    'MPI_Comm_dup',
    'MPI_Comm_dup_with_info',
    'MPI_Comm_idup',
    'MPI_Comm_idup_with_info',
    'MPI_Comm_create',
    'MPI_Comm_create_group',
    'MPI_Comm_split',
    'MPI_Comm_split_type',
    'MPI_Comm_create_from_group',

    'MPI_Intercomm_create',
    'MPI_Intercomm_create_from_groups',
    'MPI_Intercomm_merge'
]

mpi_group_creator_funcs = [
    'MPI_Comm_group',
    'MPI_Group_union',
    'MPI_Group_intersection',
    'MPI_Group_difference',
    'MPI_Group_incl',
    'MPI_Group_excl',
    'MPI_Group_range_incl',
    'MPI_Group_range_excl',
    'MPI_Group_from_session_pset'
]

mpi_collective_funcs = [
    'MPI_Barrier',
    'MPI_Bcast',
    'MPI_Gather',
    'MPI_Gatherv',
    'MPI_Scatter',
    'MPI_Scatterv',
    'MPI_Allgather',
    'MPI_Allgatherv',
    'MPI_Alltoall',
    'MPI_Alltoallv',
    'MPI_Reduce',
    'MPI_Allreduce',
    'MPI_Reduce_scatter',
    'MPI_Alltoallw',
    'MPI_Exscan',
    'MPI_Reduce_local',
    'MPI_Ibarrier',
    'MPI_Ibcast',
    'MPI_Igather',
    'MPI_Igatherv',
    'MPI_Iscatter',
    'MPI_Iscatterv',
    'MPI_Iallgather',
    'MPI_Iallgatherv',
    'MPI_Ialltoall',
    'MPI_Ialltoallv',
    'MPI_Ireduce',
    'MPI_Iallreduce',
    'MPI_Ireduce_scatter',
    'MPI_Ialltoallw',
    'MPI_Iexscan',
    'MPI_Neighbor_allgather',
    'MPI_Neighbor_allgatherv',
    'MPI_Neighbor_alltoall',
    'MPI_Neighbor_alltoallv',
    'MPI_Neighbor_alltoallw',
    'MPI_Neighbor_allgather_init',
    'MPI_Neighbor_allgatherv_init',
    'MPI_Neighbor_alltoall_init',
    'MPI_Neighbor_alltoallv_init',
    'MPI_Neighbor_alltoallw_init'
    # some persistent collectives are missing
]

mpi_ptop_funcs = [
    'MPI_Send',
    'MPI_Recv',
    'MPI_Sendrecv',
    'MPI_Sendrecv_replace',
    'MPI_Isend',
    'MPI_Irecv',
    'MPI_Test',
    'MPI_Wait',
    'MPI_Request_free',
    'MPI_Waitany',
    'MPI_Testany',
    'MPI_Waitall',
    'MPI_Testall',
    'MPI_Waitsome',
    'MPI_Testsome',
    'MPI_Cancel',
    'MPI_Request_get_status',
    'MPI_Buffer_attach',
    'MPI_Buffer_detach',
    'MPI_Iprobe',
    'MPI_Probe',
    'MPI_Bsend',
    'MPI_Ssend',
    'MPI_Rsend',
    'MPI_Bsend_init',
    'MPI_Ssend_init',
    'MPI_Rsend_init',
    'MPI_Recv_init',
    # 'MPI_Start',
    # 'MPI_Startall',
    'MPI_Send_init',
    'MPI_Sendrecv_init',
    'MPI_Sendrecv_replace',
    'MPI_Test_cancelled'
]

mpi_onesided_funcs = [
    'MPI_Win_create',
    'MPI_Win_allocate',
    'MPI_Win_allocate_shared',
    'MPI_Win_create_dynamic',
    'MPI_Win_attach',
    'MPI_Win_detach',
    'MPI_Win_free',
    'MPI_Win_shared_query',
    'MPI_Win_create_keyval',
    'MPI_Win_free_keyval',
    'MPI_Win_delete_attr',
    'MPI_Win_get_attr',
    'MPI_Win_set_attr',
    'MPI_Win_start',
    'MPI_Win_complete',
    'MPI_Win_post',
    'MPI_Win_wait',
    'MPI_Win_test',
    'MPI_Win_lock',
    'MPI_Win_unlock',
    'MPI_Win_lock_all',
    'MPI_Win_unlock_all',
    'MPI_Win_flush',
    'MPI_Win_flush_all',
    'MPI_Win_flush_local',
    'MPI_Win_flush_local_all',
    'MPI_Win_sync',
    'MPI_Get',
    'MPI_Put',
    'MPI_Rget',
    'MPI_Rput',
    'MPI_Accumulate',
    'MPI_Get_accumulate',
    'MPI_Fetch_and_op',
    'MPI_Compare_and_swap'
]

mpi_persistent_funcs = [
    'MPI_Send_init',
    'MPI_Recv_init',
    'MPI_Bsend_init',
    'MPI_Ssend_init',
    'MPI_Rsend_init',
    'MPI_Start',
    'MPI_Startall',
    'MPI_Bcast_init',
    'MPI_Gather_init',
    'MPI_Gatherv_init',
    'MPI_Scatter_init',
    'MPI_Scatterv_init',
    'MPI_Allgather_init',
    'MPI_Allgatherv_init',
    'MPI_Alltoall_init',
    'MPI_Alltoallv_init',
    'MPI_Alltoallw_init',
    'MPI_Reduce_init',
    'MPI_Allreduce_init',
    'MPI_Reduce_scatter_init',
    'MPI_Reduce_scatter_block_init',
    'MPI_Exscan_init',
    'MPI_Scan_init'
    # neighbour init
]

mpi_comm_group_funcs = [
    'MPI_Comm_create',
    'MPI_Comm_create_group',
    'MPI_Comm_split',
    'MPI_Comm_split_type',
    'MPI_Comm_dup',
    'MPI_Comm_idup',
    'MPI_Comm_clone',
    'MPI_Comm_free',
    'MPI_Comm_set_info',
    'MPI_Comm_set_errhandler',
    'MPI_Comm_get_info',
    'MPI_Comm_get_errhandler',
    'MPI_Comm_compare',
    'MPI_Comm_remote_size',
    'MPI_Comm_remote_group',
    'MPI_Group_create',
    'MPI_Group_dup',
    'MPI_Group_free',
    'MPI_Group_range_incl',
    'MPI_Group_incl',
    'MPI_Group_excl',
    'MPI_Group_translate_ranks',
    'MPI_Group_size',
    'MPI_Group_rank',
    'MPI_Group_compare',
    'MPI_Group_union',
    'MPI_Group_intersection',
    'MPI_Group_difference'
]

mpi_attribute_funcs = [
    'MPI_Comm_set_attr',
    'MPI_Comm_get_attr',
    'MPI_Type_set_attr',
    'MPI_Type_get_attr',
    'MPI_Win_set_attr',
    'MPI_Win_get_attr',
    'MPI_Comm_delete_attr',
    'MPI_Type_delete_attr',
    'MPI_Win_delete_attr',
    'MPI_Comm_create_keyval',
    'MPI_Comm_free_keyval',
    'MPI_Comm_get_attrs',
    'MPI_Comm_set_attrs',
    'MPI_Type_create_keyval',
    'MPI_Type_free_keyval',
    'MPI_Type_get_attrs',
    'MPI_Type_set_attrs',
    'MPI_Win_create_keyval',
    'MPI_Win_free_keyval',
    'MPI_Win_get_attrs',
    'MPI_Win_set_attrs'
]

mpi_topo_funcs = [
    'MPI_Cart_create',
    'MPI_Cart_get',
    'MPI_Cart_rank',
    'MPI_Cart_coords',
    'MPI_Cart_shift',
    'MPI_Cart_sub',
    'MPI_Graph_create',
    'MPI_Graph_get',
    'MPI_Graph_map',
    'MPI_Graph_neighbors',
    'MPI_Topo_test',
    'MPI_Topo_test_supported',
    'MPI_Dist_graph_create',
    'MPI_Dist_graph_create_adjacent',
    'MPI_Dist_graph_neighbors'
]

mpi_io_funcs = [
    'MPI_File_open',
    'MPI_File_close',
    'MPI_File_delete',
    'MPI_File_set_size',
    'MPI_File_get_size',
    'MPI_File_set_view',
    'MPI_File_get_view',
    'MPI_File_read',
    'MPI_File_read_all',
    'MPI_File_read_at',
    'MPI_File_read_at_all',
    'MPI_File_write',
    'MPI_File_write_all',
    'MPI_File_write_at',
    'MPI_File_write_at_all',
    'MPI_File_iread',
    'MPI_File_iread_all',
    'MPI_File_iread_at',
    'MPI_File_iread_at_all',
    'MPI_File_iwrite',
    'MPI_File_iwrite_all',
    'MPI_File_iwrite_at',
    'MPI_File_iwrite_at_all',
    'MPI_File_get_atomicity',
    'MPI_File_set_atomicity',
    'MPI_File_get_amode',
    'MPI_File_get_type_extent',
    'MPI_File_get_position',
    'MPI_File_get_byte_offset',
    'MPI_File_seek',
    'MPI_File_sync',
    'MPI_File_get_info',
    'MPI_File_set_info',
    'MPI_File_iread_shared',
    'MPI_File_iwrite_shared',
    'MPI_File_read_shared',
    'MPI_File_read_all_shared',
    'MPI_File_write_shared',
    'MPI_File_write_all_shared',
    'MPI_File_read_ordered',
    'MPI_File_read_at_all_begin',
    'MPI_File_read_at_all_end',
    'MPI_File_write_ordered',
    'MPI_File_write_at_all_begin',
    'MPI_File_write_at_all_end',
    'MPI_File_sync',
    'MPI_File_sync_all',
    'MPI_File_set_atomicity',
    'MPI_File_set_size'
]

mpi_error_funcs = [
    'MPI_Errhandler_create',
    'MPI_Errhandler_free',
    'MPI_Errhandler_get',
    'MPI_Errhandler_set',
    'MPI_Error_class',
    'MPI_Error_string',
    'MPI_Comm_create_errhandler',
    'MPI_Comm_get_errhandler',
    'MPI_Comm_set_errhandler',
    'MPI_Win_create_errhandler',
    'MPI_Win_get_errhandler',
    'MPI_Win_set_errhandler',
    'MPI_File_create_errhandler',
    'MPI_File_get_errhandler',
    'MPI_File_set_errhandler'
]

mpi_info_obj_funcs = [
    'MPI_Info_create',
    'MPI_Info_delete',
    'MPI_Info_dup',
    'MPI_Info_free',
    'MPI_Info_get',
    'MPI_Info_get_nkeys',
    'MPI_Info_get_nthkey',
    'MPI_Info_get_valuelen',
    'MPI_Info_set',
    'MPI_Info_delete_attribute',
    'MPI_Info_get_attribute',
    'MPI_Info_get_nkeys',
    'MPI_Info_get_nthkey',
    'MPI_Info_set_attribute'
]

mpi_process_mgmt_funcs = [
    'MPI_Comm_spawn',
    'MPI_Comm_spawn_multiple',
    'MPI_Comm_get_parent',
    'MPI_Comm_accept',
    'MPI_Comm_connect',
    'MPI_Comm_disconnect',
    'MPI_Open_port',
    'MPI_Close_port',
    'MPI_Publish_name',
    'MPI_Unpublish_name',
    'MPI_Lookup_name',
    'MPI_Comm_join'
]
mpi_tools_iface_funcs = [
    'MPI_T_init_thread',
    'MPI_T_finalize',
    'MPI_T_enum_get_info',
    'MPI_T_enum_get_item',
    'MPI_T_cvar_get_num',
    'MPI_T_cvar_get_info',
    'MPI_T_cvar_get_index',
    'MPI_T_cvar_handle_alloc',
    'MPI_T_cvar_handle_free',
    'MPI_T_cvar_read',
    'MPI_T_cvar_write',
    'MPI_T_pvar_get_num',
    'MPI_T_pvar_get_info',
    'MPI_T_pvar_get_index',
    'MPI_T_pvar_session_create',
    'MPI_T_pvar_session_free',
    'MPI_T_pvar_handle_alloc',
    'MPI_T_pvar_handle_free',
    'MPI_T_pvar_start',
    'MPI_T_pvar_stop',
    'MPI_T_pvar_read',
    'MPI_T_pvar_write',
    'MPI_T_pvar_reset',
    'MPI_T_pvar_readreset',
    'MPI_T_category_get_num',
    'MPI_T_category_get_info',
    'MPI_T_category_get_index',
    'MPI_T_category_get_cvars',
    'MPI_T_category_get_pvars',
    'MPI_T_category_changed'
]
mpi_predefined_collective_ops = [
    'MPI_MAX',
    'MPI_MIN',
    'MPI_SUM',
    'MPI_PROD',
    'MPI_MAXLOC',
    'MPI_MINLOC',
    'MPI_BAND',
    'MPI_BOR',
    'MPI_BXOR',
    'MPI_LAND',
    'MPI_LOR',
    'MPI_LXOR',
    'MPI_REPLACE',
    'MPI_NO_OP'
]

predefined_mpi_buf_constants = [
    'MPI_BOTTOM',
    'MPI_IN_PLACE'
]

predefined_mpi_wildcard_constants = [
    'MPI_ANY_SOURCE',
    'MPI_ANY_TAG',
]

predefined_error_handle_constants = [
    'MPI_ERRORS_ARE_FATAL',
    'MPI_ERRORS_RETURN'
]

predefined_thread_levelnstants = [
    'MPI_THREAD_SINGLE',
    'MPI_THREAD_SERIALIZED',
    'MPI_THREAD_FUNNELED',
    'MPI_THREAD_MULTIPLE'
]

predefined_mpi_other_integer_constants = [
    'MPI_PROC_NULL',
    'MPI_UNDEFINED',
    'MPI_BSEND_OVERHEAD',
    'MPI_KEYVAL_INVALID',
    'MPI_LOCK_EXCLUSIVE',
    'MPI_LOCK_SHARED',
    'MPI_ROOT',
]

predefined_mpi_null_constants = [
    'MPI_GROUP_NULL',
    'MPI_COMM_NULL',
    'MPI_DATATYPE_NULL',
    'MPI_REQUEST_NULL',
    'MPI_OP_NULL',
    'MPI_ERRHANDLER_NULL',
    'MPI_FILE_NULL',
    'MPI_INFO_NULL',
    'MPI_WIN_NULL',
    'MPI_GROUP_EMPTY',
    'MPI_ARGVS_NULL',
    'MPI_ARGV_NULL',
    'MPI_ERRCODES_IGNORE',
    'MPI_STATUSES_IGNORE',
    'MPI_STATUS_IGNORE'

]

mpi_converter_funcs = [
    'MPI_Comm_f2c',
    'MPI_Errhandler_f2c',
    'MPI_File_f2c',
    'MPI_Group_f2c',
    'MPI_Info_f2c',
    'MPI_Message_f2c',
    'MPI_Op_f2c',
    'MPI_Request_f2c',
    'MPI_Session_f2c',
    'MPI_Status_f2c',
    'MPI_Type_f2c',
    'MPI_Win_f2c',

    'MPI_Comm_c2f',
    'MPI_Errhandler_c2f',
    'MPI_File_c2f',
    'MPI_Group_c2f',
    'MPI_Info_c2f',
    'MPI_Message_c2f',
    'MPI_Op_c2f',
    'MPI_Request_c2f',
    'MPI_Session_c2f',
    'MPI_Status_c2f',
    'MPI_Type_c2f',
    'MPI_Win_c2f',
]

predefined_mpi_constants = (predefined_mpi_dtype_consants +
                            predefined_mpi_communicator_consants +
                            mpi_predefined_collective_ops +
                            mpi_optional_predefined_types +
                            predefined_mpi_buf_constants +
                            predefined_mpi_wildcard_constants +
                            predefined_error_handle_constants +
                            predefined_mpi_other_integer_constants +
                            predefined_mpi_null_constants + predefined_thread_levelnstants)

# Categories according to ScoreP
mpi_scorep_ext = ["MPI_Abort",
                  "MPI_Get_count",
                  "MPI_Get_elements",
                  "MPI_Get_elements_x",
                  "MPI_Get_processor_name",
                  "MPI_Grequest_complete",
                  "MPI_Grequest_start",
                  "MPI_Status_set_cancelled",
                  "MPI_Status_set_elements",
                  "MPI_Status_set_elements_x",
                  "MPI_Wtick",
                  "MPI_Wtime",
                  "MPI_Aint_add",
                  "MPI_Aint_diff"]

mpi_scorep_err = ["MPI_Add_error_class",
                  "MPI_Add_error_code",
                  "MPI_Add_error_string",
                  "MPI_Errhandler_create",
                  "MPI_Errhandler_free",
                  "MPI_Errhandler_get",
                  "MPI_Errhandler_set",
                  "MPI_Error_class",
                  "MPI_Error_string"]

mpi_scorep_misc = ["MPI_Address",
                   "MPI_Alloc_mem",
                   "MPI_Free_mem",
                   "MPI_Get_address",
                   "MPI_Get_version",
                   "MPI_Op_c2f",
                   "MPI_Op_commutative",
                   "MPI_Op_create",
                   "MPI_Op_f2c",
                   "MPI_Op_free",
                   "MPI_Request_c2f",
                   "MPI_Request_f2c",
                   "MPI_Request_get_status",
                   "MPI_Status_c2f",
                   "MPI_Status_f2c"]

mpi_scorep_info_custom = ["MPI_Info_c2f",
                          "MPI_Info_create",
                          "MPI_Info_delete",
                          "MPI_Info_dup",
                          "MPI_Info_f2c",
                          "MPI_Info_free",
                          "MPI_Info_get",
                          "MPI_Info_get_nkeys",
                          "MPI_Info_get_nthkey",
                          "MPI_Info_get_valuelen",
                          "MPI_Info_set"]

mpi_scorep_coll = ["MPI_Allgather",
                   "MPI_Allgatherv",
                   "MPI_Allreduce",
                   "MPI_Alltoall",
                   "MPI_Alltoallv",
                   "MPI_Alltoallw",
                   "MPI_Barrier",
                   "MPI_Bcast",
                   "MPI_Exscan",
                   "MPI_Gather",
                   "MPI_Gatherv",
                   "MPI_Iallgather",
                   "MPI_Iallgatherv",
                   "MPI_Iallreduce",
                   "MPI_Ialltoall",
                   "MPI_Ialltoallv",
                   "MPI_Ialltoallw",
                   "MPI_Ibarrier",
                   "MPI_Ibcast",
                   "MPI_Iexscan",
                   "MPI_Igather",
                   "MPI_Igatherv",
                   "MPI_Ireduce",
                   "MPI_Ireduce_scatter",
                   "MPI_Ireduce_scatter_block",
                   "MPI_Iscan",
                   "MPI_Iscatter",
                   "MPI_Iscatterv",
                   "MPI_Reduce",
                   "MPI_Reduce_local",
                   "MPI_Reduce_scatter",
                   "MPI_Reduce_scatter_block",
                   "MPI_Scan",
                   "MPI_Scatter",
                   "MPI_Scatterv"]

mpi_scorep_p2p = ["MPI_Bsend",
                  "MPI_Bsend_init",
                  "MPI_Buffer_attach",
                  "MPI_Buffer_detach",
                  "MPI_Ibsend",
                  "MPI_Improbe",
                  "MPI_Imrecv",
                  "MPI_Iprobe",
                  "MPI_Irecv",
                  "MPI_Irsend",
                  "MPI_Isend",
                  "MPI_Issend",
                  "MPI_Mprobe",
                  "MPI_Mrecv",
                  "MPI_Probe",
                  "MPI_Recv",
                  "MPI_Recv_init",
                  "MPI_Rsend",
                  "MPI_Rsend_init",
                  "MPI_Send",
                  "MPI_Send_init",
                  "MPI_Sendrecv",
                  "MPI_Sendrecv_replace",
                  "MPI_Ssend",
                  "MPI_Ssend_init"]

mpi_scorep_request = ["MPI_Cancel",
                      "MPI_Request_free",
                      "MPI_Start",
                      "MPI_Startall",
                      "MPI_Test",
                      "MPI_Test_cancelled",
                      "MPI_Testall",
                      "MPI_Testany",
                      "MPI_Testsome",
                      "MPI_Wait",
                      "MPI_Waitall",
                      "MPI_Waitany",
                      "MPI_Waitsome"]

mpi_scorep_custom_request_p2p = ["MPI_Cancel",
                                 "MPI_Request_free",
                                 "MPI_Test",
                                 "MPI_Test_cancelled",
                                 "MPI_Testall",
                                 "MPI_Testany",
                                 "MPI_Testsome",
                                 "MPI_Wait",
                                 "MPI_Waitall",
                                 "MPI_Waitany",
                                 "MPI_Waitsome"]

mpi_scorep_custom_request_persistent = set(mpi_scorep_request) - set(mpi_scorep_custom_request_p2p)

mpi_scorep_topo = ["MPI_Cart_coords",
                   "MPI_Cart_create",
                   "MPI_Cart_get",
                   "MPI_Cart_map",
                   "MPI_Cart_rank",
                   "MPI_Cart_shift",
                   "MPI_Cart_sub",
                   "MPI_Cartdim_get",
                   "MPI_Dims_create",
                   "MPI_Dist_graph_create",
                   "MPI_Dist_graph_create_adjacent",
                   "MPI_Dist_graph_neighbors",
                   "MPI_Dist_graph_neighbors_count",
                   "MPI_Graph_create",
                   "MPI_Graph_get",
                   "MPI_Graph_map",
                   "MPI_Graph_neighbors",
                   "MPI_Graph_neighbors_count",
                   "MPI_Graphdims_get",
                   "MPI_Ineighbor_allgather",
                   "MPI_Ineighbor_allgatherv",
                   "MPI_Ineighbor_alltoall",
                   "MPI_Ineighbor_alltoallv",
                   "MPI_Ineighbor_alltoallw",
                   "MPI_Neighbor_allgather",
                   "MPI_Neighbor_allgatherv",
                   "MPI_Neighbor_alltoall",
                   "MPI_Neighbor_alltoallv",
                   "MPI_Neighbor_alltoallw",
                   "MPI_Topo_test"]

mpi_scorep_spawn = ["MPI_Close_port",
                    "MPI_Comm_accept",
                    "MPI_Comm_connect",
                    "MPI_Comm_disconnect",
                    "MPI_Comm_get_parent",
                    "MPI_Comm_join",
                    "MPI_Comm_spawn",
                    "MPI_Comm_spawn_multiple",
                    "MPI_Lookup_name",
                    "MPI_Open_port",
                    "MPI_Publish_name",
                    "MPI_Unpublish_name"]

mpi_scorep_cg_ext = ["MPI_Attr_delete",
                     "MPI_Attr_get",
                     "MPI_Attr_put",
                     "MPI_Comm_create_keyval",
                     "MPI_Comm_delete_attr",
                     "MPI_Comm_free_keyval",
                     "MPI_Comm_get_attr",
                     "MPI_Comm_get_info",
                     "MPI_Comm_get_name",
                     "MPI_Comm_set_attr",
                     "MPI_Comm_set_info",
                     "MPI_Comm_set_name",
                     "MPI_Keyval_create",
                     "MPI_Keyval_free"]

mpi_scorep_cg_misc = ["MPI_Comm_c2f",
                      "MPI_Comm_f2c",
                      "MPI_Group_c2f",
                      "MPI_Group_f2c"]
mpi_scorep_cg_err = ["MPI_Comm_call_errhandler",
                     "MPI_Comm_create_errhandler",
                     "MPI_Comm_get_errhandler",
                     "MPI_Comm_set_errhandler"]
mpi_scorep_cg = ["MPI_Comm_compare",
                 "MPI_Comm_create",
                 "MPI_Comm_create_group",
                 "MPI_Comm_dup",
                 "MPI_Comm_dup_with_info",
                 "MPI_Comm_free",
                 "MPI_Comm_group",
                 "MPI_Comm_idup",
                 # "MPI_Comm_rank",
                 # "MPI_Comm_size",
                 "MPI_Comm_remote_group",
                 "MPI_Comm_remote_size",
                 "MPI_Comm_split",
                 "MPI_Comm_split_type",
                 "MPI_Comm_test_inter",
                 "MPI_Group_compare",
                 "MPI_Group_difference",
                 "MPI_Group_excl",
                 "MPI_Group_free",
                 "MPI_Group_incl",
                 "MPI_Group_intersection",
                 "MPI_Group_range_excl",
                 "MPI_Group_range_incl",
                 # "MPI_Group_rank",
                 # "MPI_Group_size",
                 "MPI_Group_translate_ranks",
                 "MPI_Group_union",
                 "MPI_Intercomm_create",
                 "MPI_Intercomm_merge"]
# unused:
mpi_scorep_cg_misc_excluded = [
    "MPI_Group_rank",
    "MPI_Group_size",
    "MPI_Comm_rank",
    "MPI_Comm_size",
]

mpi_scorep_io_misc = ["MPI_File_c2f",
                      "MPI_File_f2c"]
mpi_scorep_io_err = ["MPI_File_call_errhandler",
                     "MPI_File_create_errhandler",
                     "MPI_File_get_errhandler",
                     "MPI_File_set_errhandler"]
mpi_scorep_io = ["MPI_File_close",
                 "MPI_File_delete",
                 "MPI_File_get_amode",
                 "MPI_File_get_atomicity",
                 "MPI_File_get_byte_offset",
                 "MPI_File_get_group",
                 "MPI_File_get_info",
                 "MPI_File_get_position",
                 "MPI_File_get_position_shared",
                 "MPI_File_get_size",
                 "MPI_File_get_type_extent",
                 "MPI_File_get_view",
                 "MPI_File_iread",
                 "MPI_File_iread_all",
                 "MPI_File_iread_at",
                 "MPI_File_iread_at_all",
                 "MPI_File_iread_shared",
                 "MPI_File_iwrite",
                 "MPI_File_iwrite_all",
                 "MPI_File_iwrite_at",
                 "MPI_File_iwrite_at_all",
                 "MPI_File_iwrite_shared",
                 "MPI_File_open",
                 "MPI_File_preallocate",
                 "MPI_File_read",
                 "MPI_File_read_all",
                 "MPI_File_read_all_begin",
                 "MPI_File_read_all_end",
                 "MPI_File_read_at",
                 "MPI_File_read_at_all",
                 "MPI_File_read_at_all_begin",
                 "MPI_File_read_at_all_end",
                 "MPI_File_read_ordered",
                 "MPI_File_read_ordered_begin",
                 "MPI_File_read_ordered_end",
                 "MPI_File_read_shared",
                 "MPI_File_seek",
                 "MPI_File_seek_shared",
                 "MPI_File_set_atomicity",
                 "MPI_File_set_info",
                 "MPI_File_set_size",
                 "MPI_File_set_view",
                 "MPI_File_sync",
                 "MPI_File_write",
                 "MPI_File_write_all",
                 "MPI_File_write_all_begin",
                 "MPI_File_write_all_end",
                 "MPI_File_write_at",
                 "MPI_File_write_at_all",
                 "MPI_File_write_at_all_begin",
                 "MPI_File_write_at_all_end",
                 "MPI_File_write_ordered",
                 "MPI_File_write_ordered_begin",
                 "MPI_File_write_ordered_end",
                 "MPI_File_write_shared",
                 "MPI_Register_datarep"]

# env
mpi_scorep_env = ["MPI_Finalize",
                  "MPI_Finalized",
                  "MPI_Get_library_version",
                  "MPI_Init",
                  "MPI_Init_thread",
                  "MPI_Initialized",
                  "MPI_Is_thread_main",
                  "MPI_Query_thread"]

# type
mpi_scorep_types = ["MPI_Pack",
                    "MPI_Pack_external",
                    "MPI_Pack_external_size",
                    "MPI_Pack_size",
                    "MPI_Sizeof",
                    "MPI_Type_commit",
                    "MPI_Type_contiguous",
                    "MPI_Type_create_darray",
                    "MPI_Type_create_f90_complex",
                    "MPI_Type_create_f90_integer",
                    "MPI_Type_create_f90_real",
                    "MPI_Type_create_hindexed",
                    "MPI_Type_create_hindexed_block",
                    "MPI_Type_create_hvector",
                    "MPI_Type_create_indexed_block",
                    "MPI_Type_create_resized",
                    "MPI_Type_create_struct",
                    "MPI_Type_create_subarray",
                    "MPI_Type_dup",
                    "MPI_Type_extent",
                    "MPI_Type_free",
                    "MPI_Type_get_contents",
                    "MPI_Type_get_envelope",
                    "MPI_Type_get_extent",
                    "MPI_Type_get_extent_x",
                    "MPI_Type_get_true_extent",
                    "MPI_Type_get_true_extent_x",
                    "MPI_Type_hindexed",
                    "MPI_Type_hvector",
                    "MPI_Type_indexed",
                    "MPI_Type_lb",
                    "MPI_Type_match_size",
                    "MPI_Type_size",
                    "MPI_Type_size_x",
                    "MPI_Type_struct",
                    "MPI_Type_ub",
                    "MPI_Type_vector",
                    "MPI_Unpack",
                    "MPI_Unpack_external"]

mpi_scorep_types_constr = [
    "MPI_Type_contiguous",
    "MPI_Type_create_darray",
    "MPI_Type_create_f90_complex",
    "MPI_Type_create_f90_integer",
    "MPI_Type_create_f90_real",
    "MPI_Type_create_hindexed",
    "MPI_Type_create_hindexed_block",
    "MPI_Type_create_hvector",
    "MPI_Type_create_indexed_block",
    "MPI_Type_create_resized",
    "MPI_Type_create_struct",
    "MPI_Type_create_subarray",
    "MPI_Type_dup",
    "MPI_Type_hindexed",
    "MPI_Type_hvector",
    "MPI_Type_indexed",
    "MPI_Type_struct",
    "MPI_Type_vector"]

mpi_scorep_type_misc = ["MPI_Type_c2f",
                        "MPI_Type_f2c"]

mpi_scorep_type_ext = ["MPI_Type_create_keyval",
                       "MPI_Type_delete_attr",
                       "MPI_Type_free_keyval",
                       "MPI_Type_get_attr",
                       "MPI_Type_get_name",
                       "MPI_Type_set_attr",
                       "MPI_Type_set_name"]
# perf
mpi_scorep_perf = ['MPI_Pcontrol']
mpi_scorep_tools = ['MPI_T_pvar_handle_alloc',
                    'MPI_T_pvar_start',
                    'MPI_T_pvar_read',
                    'MPI_T_pvar_write',
                    'MPI_T_pvar_reset',
                    'MPI_T_pvar_readreset',
                    'MPI_T_category_get_num',
                    'MPI_T_category_get_info',
                    'MPI_T_category_get_cvars',
                    'MPI_T_category_get_pvars',
                    'MPI_T_category_get_categories',
                    'MPI_T_category_changed',
                    'MPI_T_cvar_get_index',
                    'MPI_T_pvar_get_index',
                    'MPI_T_category_get_index',
                    'MPI_T_pvar_handle_free',
                    'MPI_T_pvar_stop',
                    'MPI_T_pvar_session_free',
                    'MPI_T_cvar_get_num',
                    'MPI_T_init_thread',
                    'MPI_T_pvar_session_create',
                    'MPI_T_enum_get_info',
                    'MPI_T_enum_get_item',
                    'MPI_T_finalize',
                    'MPI_T_cvar_get_info',
                    'MPI_T_cvar_handle_alloc',
                    'MPI_T_cvar_handle_free',
                    'MPI_T_cvar_read',
                    'MPI_T_cvar_write',
                    'MPI_T_pvar_get_num',
                    'MPI_T_pvar_get_info']

mpi_scorep_rma = ["MPI_Accumulate",
                  "MPI_Compare_and_swap",
                  "MPI_Fetch_and_op",
                  "MPI_Get",
                  "MPI_Get_accumulate",
                  "MPI_Put",
                  "MPI_Raccumulate",
                  "MPI_Rget",
                  "MPI_Rget_accumulate",
                  "MPI_Rput",
                  "MPI_Win_allocate",
                  "MPI_Win_allocate_shared",
                  "MPI_Win_attach",
                  "MPI_Win_complete",
                  "MPI_Win_create",
                  "MPI_Win_detach",
                  "MPI_Win_create_dynamic",
                  "MPI_Win_fence",
                  "MPI_Win_free",
                  "MPI_Win_get_group",
                  "MPI_Win_lock",
                  "MPI_Win_lock_all",
                  "MPI_Win_post",
                  "MPI_Win_flush",
                  "MPI_Win_flush_all",
                  "MPI_Win_flush_local",
                  "MPI_Win_flush_local_all",
                  "MPI_Win_shared_query",
                  "MPI_Win_start",
                  "MPI_Win_sync",
                  "MPI_Win_test",
                  "MPI_Win_unlock",
                  "MPI_Win_unlock_all",
                  "MPI_Win_wait"]
mpi_scorep_rma_misc = ["MPI_Win_c2f",
                       "MPI_Win_f2c"]
mpi_scorep_rma_err = ["MPI_Win_call_errhandler",
                      "MPI_Win_create_errhandler",
                      "MPI_Win_get_errhandler",
                      "MPI_Win_set_errhandler"]
mpi_scorep_rma_ext = ["MPI_Win_create_keyval",
                      "MPI_Win_delete_attr",
                      "MPI_Win_free_keyval",
                      "MPI_Win_get_attr",
                      "MPI_Win_get_info",
                      "MPI_Win_get_name",
                      "MPI_Win_set_attr",
                      "MPI_Win_set_info",
                      "MPI_Win_set_name"]

# mpi_scorep_attrib_comm_custom = ['MPI_Comm_create_keyval', 'MPI_Comm_free_keyval', 'MPI_Comm_set_attr',
#                                  'MPI_Comm_get_attr', 'MPI_Comm_delete_attr']
# mpi_scorep_attrib_win_custom = ['MPI_Win_create_keyval', 'MPI_Win_free_keyval', 'MPI_Win_get_attr', 'MPI_Win_set_attr',
#                                 'MPI_Win_delete_attr']
# mpi_scorep_attrib_type_custom = ['MPI_Type_create_keyval', 'MPI_Type_free_keyval', 'MPI_Type_set_attr',
#                                  'MPI_Type_get_attr', 'MPI_Type_delete_attr']

mpi_persistent = set(mpi_persistent_funcs) | mpi_scorep_custom_request_persistent
mpi_attrib = set(mpi_scorep_cg_ext + mpi_scorep_type_ext + mpi_scorep_rma_ext)
mpi_info = set(mpi_scorep_info_custom)
mpi_rma = set(mpi_scorep_rma + mpi_scorep_rma_misc)
mpi_comm_group = set(mpi_scorep_cg + mpi_scorep_cg_misc)
mpi_types = set(mpi_scorep_types + mpi_scorep_type_misc)
mpi_types_constructor_only = set(mpi_scorep_types_constr)
mpi_topo = set(mpi_scorep_topo)
mpi_tools = set(mpi_scorep_tools + mpi_scorep_perf)
mpi_io = set(mpi_scorep_io + mpi_scorep_io_misc)
mpi_misc = set(mpi_scorep_misc + mpi_scorep_env)
mpi_error = set(mpi_scorep_err + mpi_scorep_cg_err + mpi_scorep_rma_err + mpi_scorep_io_err)
mpi_p2p = set(mpi_scorep_p2p + mpi_scorep_custom_request_p2p) - mpi_persistent
mpi_coll = set(mpi_scorep_coll) - mpi_persistent
mpi_request = set(mpi_scorep_request)
mpi_processm = set(mpi_scorep_spawn)
mpi_all_mpi = (mpi_rma | mpi_comm_group | mpi_types | mpi_topo |
               mpi_tools | mpi_misc | mpi_error | mpi_p2p |
               mpi_coll | mpi_request | mpi_processm | mpi_io | mpi_info | mpi_attrib | mpi_persistent)

mpi_categories = {
    'pt2pt': mpi_p2p,
    'rma': mpi_rma,
    'io': mpi_io,
    'coll': mpi_collective_funcs,
    'comm_group': mpi_comm_group,
    'types': mpi_types,
    'topo': mpi_topo,
    'persistent':mpi_persistent,
    'processmgmt': mpi_processm

}
