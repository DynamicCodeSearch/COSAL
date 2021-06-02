package edu.ncsu.haskell.parser.antlr;// Generated from HaskellParser.g4 by ANTLR 4.9.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link HaskellParser}.
 */
public interface HaskellParserListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link HaskellParser#module}.
	 * @param ctx the parse tree
	 */
	void enterModule(HaskellParser.ModuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#module}.
	 * @param ctx the parse tree
	 */
	void exitModule(HaskellParser.ModuleContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#module_content}.
	 * @param ctx the parse tree
	 */
	void enterModule_content(HaskellParser.Module_contentContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#module_content}.
	 * @param ctx the parse tree
	 */
	void exitModule_content(HaskellParser.Module_contentContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#where_module}.
	 * @param ctx the parse tree
	 */
	void enterWhere_module(HaskellParser.Where_moduleContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#where_module}.
	 * @param ctx the parse tree
	 */
	void exitWhere_module(HaskellParser.Where_moduleContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#module_body}.
	 * @param ctx the parse tree
	 */
	void enterModule_body(HaskellParser.Module_bodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#module_body}.
	 * @param ctx the parse tree
	 */
	void exitModule_body(HaskellParser.Module_bodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#pragmas}.
	 * @param ctx the parse tree
	 */
	void enterPragmas(HaskellParser.PragmasContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#pragmas}.
	 * @param ctx the parse tree
	 */
	void exitPragmas(HaskellParser.PragmasContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#pragma}.
	 * @param ctx the parse tree
	 */
	void enterPragma(HaskellParser.PragmaContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#pragma}.
	 * @param ctx the parse tree
	 */
	void exitPragma(HaskellParser.PragmaContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#language_pragma}.
	 * @param ctx the parse tree
	 */
	void enterLanguage_pragma(HaskellParser.Language_pragmaContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#language_pragma}.
	 * @param ctx the parse tree
	 */
	void exitLanguage_pragma(HaskellParser.Language_pragmaContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#options_ghc}.
	 * @param ctx the parse tree
	 */
	void enterOptions_ghc(HaskellParser.Options_ghcContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#options_ghc}.
	 * @param ctx the parse tree
	 */
	void exitOptions_ghc(HaskellParser.Options_ghcContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#simple_options}.
	 * @param ctx the parse tree
	 */
	void enterSimple_options(HaskellParser.Simple_optionsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#simple_options}.
	 * @param ctx the parse tree
	 */
	void exitSimple_options(HaskellParser.Simple_optionsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#extension}.
	 * @param ctx the parse tree
	 */
	void enterExtension(HaskellParser.ExtensionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#extension}.
	 * @param ctx the parse tree
	 */
	void exitExtension(HaskellParser.ExtensionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#body}.
	 * @param ctx the parse tree
	 */
	void enterBody(HaskellParser.BodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#body}.
	 * @param ctx the parse tree
	 */
	void exitBody(HaskellParser.BodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#impdecls}.
	 * @param ctx the parse tree
	 */
	void enterImpdecls(HaskellParser.ImpdeclsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#impdecls}.
	 * @param ctx the parse tree
	 */
	void exitImpdecls(HaskellParser.ImpdeclsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#exports}.
	 * @param ctx the parse tree
	 */
	void enterExports(HaskellParser.ExportsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#exports}.
	 * @param ctx the parse tree
	 */
	void exitExports(HaskellParser.ExportsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#exprt}.
	 * @param ctx the parse tree
	 */
	void enterExprt(HaskellParser.ExprtContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#exprt}.
	 * @param ctx the parse tree
	 */
	void exitExprt(HaskellParser.ExprtContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#impdecl}.
	 * @param ctx the parse tree
	 */
	void enterImpdecl(HaskellParser.ImpdeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#impdecl}.
	 * @param ctx the parse tree
	 */
	void exitImpdecl(HaskellParser.ImpdeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#impspec}.
	 * @param ctx the parse tree
	 */
	void enterImpspec(HaskellParser.ImpspecContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#impspec}.
	 * @param ctx the parse tree
	 */
	void exitImpspec(HaskellParser.ImpspecContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#himport}.
	 * @param ctx the parse tree
	 */
	void enterHimport(HaskellParser.HimportContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#himport}.
	 * @param ctx the parse tree
	 */
	void exitHimport(HaskellParser.HimportContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#cname}.
	 * @param ctx the parse tree
	 */
	void enterCname(HaskellParser.CnameContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#cname}.
	 * @param ctx the parse tree
	 */
	void exitCname(HaskellParser.CnameContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#fixity}.
	 * @param ctx the parse tree
	 */
	void enterFixity(HaskellParser.FixityContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#fixity}.
	 * @param ctx the parse tree
	 */
	void exitFixity(HaskellParser.FixityContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#ops}.
	 * @param ctx the parse tree
	 */
	void enterOps(HaskellParser.OpsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#ops}.
	 * @param ctx the parse tree
	 */
	void exitOps(HaskellParser.OpsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#topdecls}.
	 * @param ctx the parse tree
	 */
	void enterTopdecls(HaskellParser.TopdeclsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#topdecls}.
	 * @param ctx the parse tree
	 */
	void exitTopdecls(HaskellParser.TopdeclsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#topdecl}.
	 * @param ctx the parse tree
	 */
	void enterTopdecl(HaskellParser.TopdeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#topdecl}.
	 * @param ctx the parse tree
	 */
	void exitTopdecl(HaskellParser.TopdeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#cl_decl}.
	 * @param ctx the parse tree
	 */
	void enterCl_decl(HaskellParser.Cl_declContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#cl_decl}.
	 * @param ctx the parse tree
	 */
	void exitCl_decl(HaskellParser.Cl_declContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#ty_decl}.
	 * @param ctx the parse tree
	 */
	void enterTy_decl(HaskellParser.Ty_declContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#ty_decl}.
	 * @param ctx the parse tree
	 */
	void exitTy_decl(HaskellParser.Ty_declContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#standalone_kind_sig}.
	 * @param ctx the parse tree
	 */
	void enterStandalone_kind_sig(HaskellParser.Standalone_kind_sigContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#standalone_kind_sig}.
	 * @param ctx the parse tree
	 */
	void exitStandalone_kind_sig(HaskellParser.Standalone_kind_sigContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#sks_vars}.
	 * @param ctx the parse tree
	 */
	void enterSks_vars(HaskellParser.Sks_varsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#sks_vars}.
	 * @param ctx the parse tree
	 */
	void exitSks_vars(HaskellParser.Sks_varsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#inst_decl}.
	 * @param ctx the parse tree
	 */
	void enterInst_decl(HaskellParser.Inst_declContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#inst_decl}.
	 * @param ctx the parse tree
	 */
	void exitInst_decl(HaskellParser.Inst_declContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#overlap_pragma}.
	 * @param ctx the parse tree
	 */
	void enterOverlap_pragma(HaskellParser.Overlap_pragmaContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#overlap_pragma}.
	 * @param ctx the parse tree
	 */
	void exitOverlap_pragma(HaskellParser.Overlap_pragmaContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#deriv_strategy_no_via}.
	 * @param ctx the parse tree
	 */
	void enterDeriv_strategy_no_via(HaskellParser.Deriv_strategy_no_viaContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#deriv_strategy_no_via}.
	 * @param ctx the parse tree
	 */
	void exitDeriv_strategy_no_via(HaskellParser.Deriv_strategy_no_viaContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#deriv_strategy_via}.
	 * @param ctx the parse tree
	 */
	void enterDeriv_strategy_via(HaskellParser.Deriv_strategy_viaContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#deriv_strategy_via}.
	 * @param ctx the parse tree
	 */
	void exitDeriv_strategy_via(HaskellParser.Deriv_strategy_viaContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#deriv_standalone_strategy}.
	 * @param ctx the parse tree
	 */
	void enterDeriv_standalone_strategy(HaskellParser.Deriv_standalone_strategyContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#deriv_standalone_strategy}.
	 * @param ctx the parse tree
	 */
	void exitDeriv_standalone_strategy(HaskellParser.Deriv_standalone_strategyContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#opt_injective_info}.
	 * @param ctx the parse tree
	 */
	void enterOpt_injective_info(HaskellParser.Opt_injective_infoContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#opt_injective_info}.
	 * @param ctx the parse tree
	 */
	void exitOpt_injective_info(HaskellParser.Opt_injective_infoContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#injectivity_cond}.
	 * @param ctx the parse tree
	 */
	void enterInjectivity_cond(HaskellParser.Injectivity_condContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#injectivity_cond}.
	 * @param ctx the parse tree
	 */
	void exitInjectivity_cond(HaskellParser.Injectivity_condContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#inj_varids}.
	 * @param ctx the parse tree
	 */
	void enterInj_varids(HaskellParser.Inj_varidsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#inj_varids}.
	 * @param ctx the parse tree
	 */
	void exitInj_varids(HaskellParser.Inj_varidsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#where_type_family}.
	 * @param ctx the parse tree
	 */
	void enterWhere_type_family(HaskellParser.Where_type_familyContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#where_type_family}.
	 * @param ctx the parse tree
	 */
	void exitWhere_type_family(HaskellParser.Where_type_familyContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#ty_fam_inst_eqn_list}.
	 * @param ctx the parse tree
	 */
	void enterTy_fam_inst_eqn_list(HaskellParser.Ty_fam_inst_eqn_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#ty_fam_inst_eqn_list}.
	 * @param ctx the parse tree
	 */
	void exitTy_fam_inst_eqn_list(HaskellParser.Ty_fam_inst_eqn_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#ty_fam_inst_eqns}.
	 * @param ctx the parse tree
	 */
	void enterTy_fam_inst_eqns(HaskellParser.Ty_fam_inst_eqnsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#ty_fam_inst_eqns}.
	 * @param ctx the parse tree
	 */
	void exitTy_fam_inst_eqns(HaskellParser.Ty_fam_inst_eqnsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#ty_fam_inst_eqn}.
	 * @param ctx the parse tree
	 */
	void enterTy_fam_inst_eqn(HaskellParser.Ty_fam_inst_eqnContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#ty_fam_inst_eqn}.
	 * @param ctx the parse tree
	 */
	void exitTy_fam_inst_eqn(HaskellParser.Ty_fam_inst_eqnContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#at_decl_cls}.
	 * @param ctx the parse tree
	 */
	void enterAt_decl_cls(HaskellParser.At_decl_clsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#at_decl_cls}.
	 * @param ctx the parse tree
	 */
	void exitAt_decl_cls(HaskellParser.At_decl_clsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#at_decl_inst}.
	 * @param ctx the parse tree
	 */
	void enterAt_decl_inst(HaskellParser.At_decl_instContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#at_decl_inst}.
	 * @param ctx the parse tree
	 */
	void exitAt_decl_inst(HaskellParser.At_decl_instContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#opt_kind_sig}.
	 * @param ctx the parse tree
	 */
	void enterOpt_kind_sig(HaskellParser.Opt_kind_sigContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#opt_kind_sig}.
	 * @param ctx the parse tree
	 */
	void exitOpt_kind_sig(HaskellParser.Opt_kind_sigContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#opt_datafam_kind_sig}.
	 * @param ctx the parse tree
	 */
	void enterOpt_datafam_kind_sig(HaskellParser.Opt_datafam_kind_sigContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#opt_datafam_kind_sig}.
	 * @param ctx the parse tree
	 */
	void exitOpt_datafam_kind_sig(HaskellParser.Opt_datafam_kind_sigContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#opt_tyfam_kind_sig}.
	 * @param ctx the parse tree
	 */
	void enterOpt_tyfam_kind_sig(HaskellParser.Opt_tyfam_kind_sigContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#opt_tyfam_kind_sig}.
	 * @param ctx the parse tree
	 */
	void exitOpt_tyfam_kind_sig(HaskellParser.Opt_tyfam_kind_sigContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#opt_at_kind_inj_sig}.
	 * @param ctx the parse tree
	 */
	void enterOpt_at_kind_inj_sig(HaskellParser.Opt_at_kind_inj_sigContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#opt_at_kind_inj_sig}.
	 * @param ctx the parse tree
	 */
	void exitOpt_at_kind_inj_sig(HaskellParser.Opt_at_kind_inj_sigContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#tycl_hdr}.
	 * @param ctx the parse tree
	 */
	void enterTycl_hdr(HaskellParser.Tycl_hdrContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#tycl_hdr}.
	 * @param ctx the parse tree
	 */
	void exitTycl_hdr(HaskellParser.Tycl_hdrContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#tycl_hdr_inst}.
	 * @param ctx the parse tree
	 */
	void enterTycl_hdr_inst(HaskellParser.Tycl_hdr_instContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#tycl_hdr_inst}.
	 * @param ctx the parse tree
	 */
	void exitTycl_hdr_inst(HaskellParser.Tycl_hdr_instContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#capi_ctype}.
	 * @param ctx the parse tree
	 */
	void enterCapi_ctype(HaskellParser.Capi_ctypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#capi_ctype}.
	 * @param ctx the parse tree
	 */
	void exitCapi_ctype(HaskellParser.Capi_ctypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#standalone_deriving}.
	 * @param ctx the parse tree
	 */
	void enterStandalone_deriving(HaskellParser.Standalone_derivingContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#standalone_deriving}.
	 * @param ctx the parse tree
	 */
	void exitStandalone_deriving(HaskellParser.Standalone_derivingContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#role_annot}.
	 * @param ctx the parse tree
	 */
	void enterRole_annot(HaskellParser.Role_annotContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#role_annot}.
	 * @param ctx the parse tree
	 */
	void exitRole_annot(HaskellParser.Role_annotContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#roles}.
	 * @param ctx the parse tree
	 */
	void enterRoles(HaskellParser.RolesContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#roles}.
	 * @param ctx the parse tree
	 */
	void exitRoles(HaskellParser.RolesContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#role}.
	 * @param ctx the parse tree
	 */
	void enterRole(HaskellParser.RoleContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#role}.
	 * @param ctx the parse tree
	 */
	void exitRole(HaskellParser.RoleContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#pattern_synonym_decl}.
	 * @param ctx the parse tree
	 */
	void enterPattern_synonym_decl(HaskellParser.Pattern_synonym_declContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#pattern_synonym_decl}.
	 * @param ctx the parse tree
	 */
	void exitPattern_synonym_decl(HaskellParser.Pattern_synonym_declContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#pattern_synonym_lhs}.
	 * @param ctx the parse tree
	 */
	void enterPattern_synonym_lhs(HaskellParser.Pattern_synonym_lhsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#pattern_synonym_lhs}.
	 * @param ctx the parse tree
	 */
	void exitPattern_synonym_lhs(HaskellParser.Pattern_synonym_lhsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#hvars}.
	 * @param ctx the parse tree
	 */
	void enterHvars(HaskellParser.HvarsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#hvars}.
	 * @param ctx the parse tree
	 */
	void exitHvars(HaskellParser.HvarsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#cvars}.
	 * @param ctx the parse tree
	 */
	void enterCvars(HaskellParser.CvarsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#cvars}.
	 * @param ctx the parse tree
	 */
	void exitCvars(HaskellParser.CvarsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#where_decls}.
	 * @param ctx the parse tree
	 */
	void enterWhere_decls(HaskellParser.Where_declsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#where_decls}.
	 * @param ctx the parse tree
	 */
	void exitWhere_decls(HaskellParser.Where_declsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#pattern_synonym_sig}.
	 * @param ctx the parse tree
	 */
	void enterPattern_synonym_sig(HaskellParser.Pattern_synonym_sigContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#pattern_synonym_sig}.
	 * @param ctx the parse tree
	 */
	void exitPattern_synonym_sig(HaskellParser.Pattern_synonym_sigContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#decl_cls}.
	 * @param ctx the parse tree
	 */
	void enterDecl_cls(HaskellParser.Decl_clsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#decl_cls}.
	 * @param ctx the parse tree
	 */
	void exitDecl_cls(HaskellParser.Decl_clsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#decls_cls}.
	 * @param ctx the parse tree
	 */
	void enterDecls_cls(HaskellParser.Decls_clsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#decls_cls}.
	 * @param ctx the parse tree
	 */
	void exitDecls_cls(HaskellParser.Decls_clsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#decllist_cls}.
	 * @param ctx the parse tree
	 */
	void enterDecllist_cls(HaskellParser.Decllist_clsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#decllist_cls}.
	 * @param ctx the parse tree
	 */
	void exitDecllist_cls(HaskellParser.Decllist_clsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#where_cls}.
	 * @param ctx the parse tree
	 */
	void enterWhere_cls(HaskellParser.Where_clsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#where_cls}.
	 * @param ctx the parse tree
	 */
	void exitWhere_cls(HaskellParser.Where_clsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#decl_inst}.
	 * @param ctx the parse tree
	 */
	void enterDecl_inst(HaskellParser.Decl_instContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#decl_inst}.
	 * @param ctx the parse tree
	 */
	void exitDecl_inst(HaskellParser.Decl_instContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#decls_inst}.
	 * @param ctx the parse tree
	 */
	void enterDecls_inst(HaskellParser.Decls_instContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#decls_inst}.
	 * @param ctx the parse tree
	 */
	void exitDecls_inst(HaskellParser.Decls_instContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#decllist_inst}.
	 * @param ctx the parse tree
	 */
	void enterDecllist_inst(HaskellParser.Decllist_instContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#decllist_inst}.
	 * @param ctx the parse tree
	 */
	void exitDecllist_inst(HaskellParser.Decllist_instContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#where_inst}.
	 * @param ctx the parse tree
	 */
	void enterWhere_inst(HaskellParser.Where_instContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#where_inst}.
	 * @param ctx the parse tree
	 */
	void exitWhere_inst(HaskellParser.Where_instContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#decls}.
	 * @param ctx the parse tree
	 */
	void enterDecls(HaskellParser.DeclsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#decls}.
	 * @param ctx the parse tree
	 */
	void exitDecls(HaskellParser.DeclsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#decllist}.
	 * @param ctx the parse tree
	 */
	void enterDecllist(HaskellParser.DecllistContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#decllist}.
	 * @param ctx the parse tree
	 */
	void exitDecllist(HaskellParser.DecllistContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#binds}.
	 * @param ctx the parse tree
	 */
	void enterBinds(HaskellParser.BindsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#binds}.
	 * @param ctx the parse tree
	 */
	void exitBinds(HaskellParser.BindsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#wherebinds}.
	 * @param ctx the parse tree
	 */
	void enterWherebinds(HaskellParser.WherebindsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#wherebinds}.
	 * @param ctx the parse tree
	 */
	void exitWherebinds(HaskellParser.WherebindsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#rules}.
	 * @param ctx the parse tree
	 */
	void enterRules(HaskellParser.RulesContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#rules}.
	 * @param ctx the parse tree
	 */
	void exitRules(HaskellParser.RulesContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#pragma_rule}.
	 * @param ctx the parse tree
	 */
	void enterPragma_rule(HaskellParser.Pragma_ruleContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#pragma_rule}.
	 * @param ctx the parse tree
	 */
	void exitPragma_rule(HaskellParser.Pragma_ruleContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#rule_activation_marker}.
	 * @param ctx the parse tree
	 */
	void enterRule_activation_marker(HaskellParser.Rule_activation_markerContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#rule_activation_marker}.
	 * @param ctx the parse tree
	 */
	void exitRule_activation_marker(HaskellParser.Rule_activation_markerContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#rule_activation}.
	 * @param ctx the parse tree
	 */
	void enterRule_activation(HaskellParser.Rule_activationContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#rule_activation}.
	 * @param ctx the parse tree
	 */
	void exitRule_activation(HaskellParser.Rule_activationContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#rule_foralls}.
	 * @param ctx the parse tree
	 */
	void enterRule_foralls(HaskellParser.Rule_forallsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#rule_foralls}.
	 * @param ctx the parse tree
	 */
	void exitRule_foralls(HaskellParser.Rule_forallsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#rule_vars}.
	 * @param ctx the parse tree
	 */
	void enterRule_vars(HaskellParser.Rule_varsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#rule_vars}.
	 * @param ctx the parse tree
	 */
	void exitRule_vars(HaskellParser.Rule_varsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#rule_var}.
	 * @param ctx the parse tree
	 */
	void enterRule_var(HaskellParser.Rule_varContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#rule_var}.
	 * @param ctx the parse tree
	 */
	void exitRule_var(HaskellParser.Rule_varContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#warnings}.
	 * @param ctx the parse tree
	 */
	void enterWarnings(HaskellParser.WarningsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#warnings}.
	 * @param ctx the parse tree
	 */
	void exitWarnings(HaskellParser.WarningsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#pragma_warning}.
	 * @param ctx the parse tree
	 */
	void enterPragma_warning(HaskellParser.Pragma_warningContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#pragma_warning}.
	 * @param ctx the parse tree
	 */
	void exitPragma_warning(HaskellParser.Pragma_warningContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#deprecations}.
	 * @param ctx the parse tree
	 */
	void enterDeprecations(HaskellParser.DeprecationsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#deprecations}.
	 * @param ctx the parse tree
	 */
	void exitDeprecations(HaskellParser.DeprecationsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#pragma_deprecation}.
	 * @param ctx the parse tree
	 */
	void enterPragma_deprecation(HaskellParser.Pragma_deprecationContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#pragma_deprecation}.
	 * @param ctx the parse tree
	 */
	void exitPragma_deprecation(HaskellParser.Pragma_deprecationContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#strings}.
	 * @param ctx the parse tree
	 */
	void enterStrings(HaskellParser.StringsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#strings}.
	 * @param ctx the parse tree
	 */
	void exitStrings(HaskellParser.StringsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#stringlist}.
	 * @param ctx the parse tree
	 */
	void enterStringlist(HaskellParser.StringlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#stringlist}.
	 * @param ctx the parse tree
	 */
	void exitStringlist(HaskellParser.StringlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#annotation}.
	 * @param ctx the parse tree
	 */
	void enterAnnotation(HaskellParser.AnnotationContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#annotation}.
	 * @param ctx the parse tree
	 */
	void exitAnnotation(HaskellParser.AnnotationContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#fdecl}.
	 * @param ctx the parse tree
	 */
	void enterFdecl(HaskellParser.FdeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#fdecl}.
	 * @param ctx the parse tree
	 */
	void exitFdecl(HaskellParser.FdeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#callconv}.
	 * @param ctx the parse tree
	 */
	void enterCallconv(HaskellParser.CallconvContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#callconv}.
	 * @param ctx the parse tree
	 */
	void exitCallconv(HaskellParser.CallconvContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#safety}.
	 * @param ctx the parse tree
	 */
	void enterSafety(HaskellParser.SafetyContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#safety}.
	 * @param ctx the parse tree
	 */
	void exitSafety(HaskellParser.SafetyContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#fspec}.
	 * @param ctx the parse tree
	 */
	void enterFspec(HaskellParser.FspecContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#fspec}.
	 * @param ctx the parse tree
	 */
	void exitFspec(HaskellParser.FspecContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#opt_sig}.
	 * @param ctx the parse tree
	 */
	void enterOpt_sig(HaskellParser.Opt_sigContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#opt_sig}.
	 * @param ctx the parse tree
	 */
	void exitOpt_sig(HaskellParser.Opt_sigContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#opt_tyconsig}.
	 * @param ctx the parse tree
	 */
	void enterOpt_tyconsig(HaskellParser.Opt_tyconsigContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#opt_tyconsig}.
	 * @param ctx the parse tree
	 */
	void exitOpt_tyconsig(HaskellParser.Opt_tyconsigContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#sigtype}.
	 * @param ctx the parse tree
	 */
	void enterSigtype(HaskellParser.SigtypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#sigtype}.
	 * @param ctx the parse tree
	 */
	void exitSigtype(HaskellParser.SigtypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#sigtypedoc}.
	 * @param ctx the parse tree
	 */
	void enterSigtypedoc(HaskellParser.SigtypedocContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#sigtypedoc}.
	 * @param ctx the parse tree
	 */
	void exitSigtypedoc(HaskellParser.SigtypedocContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#sig_vars}.
	 * @param ctx the parse tree
	 */
	void enterSig_vars(HaskellParser.Sig_varsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#sig_vars}.
	 * @param ctx the parse tree
	 */
	void exitSig_vars(HaskellParser.Sig_varsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#sigtypes1}.
	 * @param ctx the parse tree
	 */
	void enterSigtypes1(HaskellParser.Sigtypes1Context ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#sigtypes1}.
	 * @param ctx the parse tree
	 */
	void exitSigtypes1(HaskellParser.Sigtypes1Context ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#unpackedness}.
	 * @param ctx the parse tree
	 */
	void enterUnpackedness(HaskellParser.UnpackednessContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#unpackedness}.
	 * @param ctx the parse tree
	 */
	void exitUnpackedness(HaskellParser.UnpackednessContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#forall_vis_flag}.
	 * @param ctx the parse tree
	 */
	void enterForall_vis_flag(HaskellParser.Forall_vis_flagContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#forall_vis_flag}.
	 * @param ctx the parse tree
	 */
	void exitForall_vis_flag(HaskellParser.Forall_vis_flagContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#ktype}.
	 * @param ctx the parse tree
	 */
	void enterKtype(HaskellParser.KtypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#ktype}.
	 * @param ctx the parse tree
	 */
	void exitKtype(HaskellParser.KtypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#ktypedoc}.
	 * @param ctx the parse tree
	 */
	void enterKtypedoc(HaskellParser.KtypedocContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#ktypedoc}.
	 * @param ctx the parse tree
	 */
	void exitKtypedoc(HaskellParser.KtypedocContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#ctype}.
	 * @param ctx the parse tree
	 */
	void enterCtype(HaskellParser.CtypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#ctype}.
	 * @param ctx the parse tree
	 */
	void exitCtype(HaskellParser.CtypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#ctypedoc}.
	 * @param ctx the parse tree
	 */
	void enterCtypedoc(HaskellParser.CtypedocContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#ctypedoc}.
	 * @param ctx the parse tree
	 */
	void exitCtypedoc(HaskellParser.CtypedocContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#tycl_context}.
	 * @param ctx the parse tree
	 */
	void enterTycl_context(HaskellParser.Tycl_contextContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#tycl_context}.
	 * @param ctx the parse tree
	 */
	void exitTycl_context(HaskellParser.Tycl_contextContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#constr_context}.
	 * @param ctx the parse tree
	 */
	void enterConstr_context(HaskellParser.Constr_contextContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#constr_context}.
	 * @param ctx the parse tree
	 */
	void exitConstr_context(HaskellParser.Constr_contextContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#htype}.
	 * @param ctx the parse tree
	 */
	void enterHtype(HaskellParser.HtypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#htype}.
	 * @param ctx the parse tree
	 */
	void exitHtype(HaskellParser.HtypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#typedoc}.
	 * @param ctx the parse tree
	 */
	void enterTypedoc(HaskellParser.TypedocContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#typedoc}.
	 * @param ctx the parse tree
	 */
	void exitTypedoc(HaskellParser.TypedocContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#constr_btype}.
	 * @param ctx the parse tree
	 */
	void enterConstr_btype(HaskellParser.Constr_btypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#constr_btype}.
	 * @param ctx the parse tree
	 */
	void exitConstr_btype(HaskellParser.Constr_btypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#constr_tyapps}.
	 * @param ctx the parse tree
	 */
	void enterConstr_tyapps(HaskellParser.Constr_tyappsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#constr_tyapps}.
	 * @param ctx the parse tree
	 */
	void exitConstr_tyapps(HaskellParser.Constr_tyappsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#constr_tyapp}.
	 * @param ctx the parse tree
	 */
	void enterConstr_tyapp(HaskellParser.Constr_tyappContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#constr_tyapp}.
	 * @param ctx the parse tree
	 */
	void exitConstr_tyapp(HaskellParser.Constr_tyappContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#btype}.
	 * @param ctx the parse tree
	 */
	void enterBtype(HaskellParser.BtypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#btype}.
	 * @param ctx the parse tree
	 */
	void exitBtype(HaskellParser.BtypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#tyapps}.
	 * @param ctx the parse tree
	 */
	void enterTyapps(HaskellParser.TyappsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#tyapps}.
	 * @param ctx the parse tree
	 */
	void exitTyapps(HaskellParser.TyappsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#tyapp}.
	 * @param ctx the parse tree
	 */
	void enterTyapp(HaskellParser.TyappContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#tyapp}.
	 * @param ctx the parse tree
	 */
	void exitTyapp(HaskellParser.TyappContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#atype}.
	 * @param ctx the parse tree
	 */
	void enterAtype(HaskellParser.AtypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#atype}.
	 * @param ctx the parse tree
	 */
	void exitAtype(HaskellParser.AtypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#inst_type}.
	 * @param ctx the parse tree
	 */
	void enterInst_type(HaskellParser.Inst_typeContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#inst_type}.
	 * @param ctx the parse tree
	 */
	void exitInst_type(HaskellParser.Inst_typeContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#deriv_types}.
	 * @param ctx the parse tree
	 */
	void enterDeriv_types(HaskellParser.Deriv_typesContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#deriv_types}.
	 * @param ctx the parse tree
	 */
	void exitDeriv_types(HaskellParser.Deriv_typesContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#comma_types}.
	 * @param ctx the parse tree
	 */
	void enterComma_types(HaskellParser.Comma_typesContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#comma_types}.
	 * @param ctx the parse tree
	 */
	void exitComma_types(HaskellParser.Comma_typesContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#bar_types2}.
	 * @param ctx the parse tree
	 */
	void enterBar_types2(HaskellParser.Bar_types2Context ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#bar_types2}.
	 * @param ctx the parse tree
	 */
	void exitBar_types2(HaskellParser.Bar_types2Context ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#tv_bndrs}.
	 * @param ctx the parse tree
	 */
	void enterTv_bndrs(HaskellParser.Tv_bndrsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#tv_bndrs}.
	 * @param ctx the parse tree
	 */
	void exitTv_bndrs(HaskellParser.Tv_bndrsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#tv_bndr}.
	 * @param ctx the parse tree
	 */
	void enterTv_bndr(HaskellParser.Tv_bndrContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#tv_bndr}.
	 * @param ctx the parse tree
	 */
	void exitTv_bndr(HaskellParser.Tv_bndrContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#tv_bndr_no_braces}.
	 * @param ctx the parse tree
	 */
	void enterTv_bndr_no_braces(HaskellParser.Tv_bndr_no_bracesContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#tv_bndr_no_braces}.
	 * @param ctx the parse tree
	 */
	void exitTv_bndr_no_braces(HaskellParser.Tv_bndr_no_bracesContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#fds}.
	 * @param ctx the parse tree
	 */
	void enterFds(HaskellParser.FdsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#fds}.
	 * @param ctx the parse tree
	 */
	void exitFds(HaskellParser.FdsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#fds1}.
	 * @param ctx the parse tree
	 */
	void enterFds1(HaskellParser.Fds1Context ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#fds1}.
	 * @param ctx the parse tree
	 */
	void exitFds1(HaskellParser.Fds1Context ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#fd}.
	 * @param ctx the parse tree
	 */
	void enterFd(HaskellParser.FdContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#fd}.
	 * @param ctx the parse tree
	 */
	void exitFd(HaskellParser.FdContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#varids0}.
	 * @param ctx the parse tree
	 */
	void enterVarids0(HaskellParser.Varids0Context ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#varids0}.
	 * @param ctx the parse tree
	 */
	void exitVarids0(HaskellParser.Varids0Context ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#kind}.
	 * @param ctx the parse tree
	 */
	void enterKind(HaskellParser.KindContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#kind}.
	 * @param ctx the parse tree
	 */
	void exitKind(HaskellParser.KindContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#gadt_constrlist}.
	 * @param ctx the parse tree
	 */
	void enterGadt_constrlist(HaskellParser.Gadt_constrlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#gadt_constrlist}.
	 * @param ctx the parse tree
	 */
	void exitGadt_constrlist(HaskellParser.Gadt_constrlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#gadt_constrs}.
	 * @param ctx the parse tree
	 */
	void enterGadt_constrs(HaskellParser.Gadt_constrsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#gadt_constrs}.
	 * @param ctx the parse tree
	 */
	void exitGadt_constrs(HaskellParser.Gadt_constrsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#gadt_constr_with_doc}.
	 * @param ctx the parse tree
	 */
	void enterGadt_constr_with_doc(HaskellParser.Gadt_constr_with_docContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#gadt_constr_with_doc}.
	 * @param ctx the parse tree
	 */
	void exitGadt_constr_with_doc(HaskellParser.Gadt_constr_with_docContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#gadt_constr}.
	 * @param ctx the parse tree
	 */
	void enterGadt_constr(HaskellParser.Gadt_constrContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#gadt_constr}.
	 * @param ctx the parse tree
	 */
	void exitGadt_constr(HaskellParser.Gadt_constrContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#constrs}.
	 * @param ctx the parse tree
	 */
	void enterConstrs(HaskellParser.ConstrsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#constrs}.
	 * @param ctx the parse tree
	 */
	void exitConstrs(HaskellParser.ConstrsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#constrs1}.
	 * @param ctx the parse tree
	 */
	void enterConstrs1(HaskellParser.Constrs1Context ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#constrs1}.
	 * @param ctx the parse tree
	 */
	void exitConstrs1(HaskellParser.Constrs1Context ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#constr}.
	 * @param ctx the parse tree
	 */
	void enterConstr(HaskellParser.ConstrContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#constr}.
	 * @param ctx the parse tree
	 */
	void exitConstr(HaskellParser.ConstrContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#forall}.
	 * @param ctx the parse tree
	 */
	void enterForall(HaskellParser.ForallContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#forall}.
	 * @param ctx the parse tree
	 */
	void exitForall(HaskellParser.ForallContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#constr_stuff}.
	 * @param ctx the parse tree
	 */
	void enterConstr_stuff(HaskellParser.Constr_stuffContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#constr_stuff}.
	 * @param ctx the parse tree
	 */
	void exitConstr_stuff(HaskellParser.Constr_stuffContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#fielddecls}.
	 * @param ctx the parse tree
	 */
	void enterFielddecls(HaskellParser.FielddeclsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#fielddecls}.
	 * @param ctx the parse tree
	 */
	void exitFielddecls(HaskellParser.FielddeclsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#fielddecl}.
	 * @param ctx the parse tree
	 */
	void enterFielddecl(HaskellParser.FielddeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#fielddecl}.
	 * @param ctx the parse tree
	 */
	void exitFielddecl(HaskellParser.FielddeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#derivings}.
	 * @param ctx the parse tree
	 */
	void enterDerivings(HaskellParser.DerivingsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#derivings}.
	 * @param ctx the parse tree
	 */
	void exitDerivings(HaskellParser.DerivingsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#deriving}.
	 * @param ctx the parse tree
	 */
	void enterDeriving(HaskellParser.DerivingContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#deriving}.
	 * @param ctx the parse tree
	 */
	void exitDeriving(HaskellParser.DerivingContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#deriv_clause_types}.
	 * @param ctx the parse tree
	 */
	void enterDeriv_clause_types(HaskellParser.Deriv_clause_typesContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#deriv_clause_types}.
	 * @param ctx the parse tree
	 */
	void exitDeriv_clause_types(HaskellParser.Deriv_clause_typesContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#decl_no_th}.
	 * @param ctx the parse tree
	 */
	void enterDecl_no_th(HaskellParser.Decl_no_thContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#decl_no_th}.
	 * @param ctx the parse tree
	 */
	void exitDecl_no_th(HaskellParser.Decl_no_thContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#decl}.
	 * @param ctx the parse tree
	 */
	void enterDecl(HaskellParser.DeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#decl}.
	 * @param ctx the parse tree
	 */
	void exitDecl(HaskellParser.DeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#rhs}.
	 * @param ctx the parse tree
	 */
	void enterRhs(HaskellParser.RhsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#rhs}.
	 * @param ctx the parse tree
	 */
	void exitRhs(HaskellParser.RhsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#gdrhs}.
	 * @param ctx the parse tree
	 */
	void enterGdrhs(HaskellParser.GdrhsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#gdrhs}.
	 * @param ctx the parse tree
	 */
	void exitGdrhs(HaskellParser.GdrhsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#gdrh}.
	 * @param ctx the parse tree
	 */
	void enterGdrh(HaskellParser.GdrhContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#gdrh}.
	 * @param ctx the parse tree
	 */
	void exitGdrh(HaskellParser.GdrhContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#sigdecl}.
	 * @param ctx the parse tree
	 */
	void enterSigdecl(HaskellParser.SigdeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#sigdecl}.
	 * @param ctx the parse tree
	 */
	void exitSigdecl(HaskellParser.SigdeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#activation}.
	 * @param ctx the parse tree
	 */
	void enterActivation(HaskellParser.ActivationContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#activation}.
	 * @param ctx the parse tree
	 */
	void exitActivation(HaskellParser.ActivationContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#th_quasiquote}.
	 * @param ctx the parse tree
	 */
	void enterTh_quasiquote(HaskellParser.Th_quasiquoteContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#th_quasiquote}.
	 * @param ctx the parse tree
	 */
	void exitTh_quasiquote(HaskellParser.Th_quasiquoteContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#th_qquasiquote}.
	 * @param ctx the parse tree
	 */
	void enterTh_qquasiquote(HaskellParser.Th_qquasiquoteContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#th_qquasiquote}.
	 * @param ctx the parse tree
	 */
	void exitTh_qquasiquote(HaskellParser.Th_qquasiquoteContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#quasiquote}.
	 * @param ctx the parse tree
	 */
	void enterQuasiquote(HaskellParser.QuasiquoteContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#quasiquote}.
	 * @param ctx the parse tree
	 */
	void exitQuasiquote(HaskellParser.QuasiquoteContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterExp(HaskellParser.ExpContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitExp(HaskellParser.ExpContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#infixexp}.
	 * @param ctx the parse tree
	 */
	void enterInfixexp(HaskellParser.InfixexpContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#infixexp}.
	 * @param ctx the parse tree
	 */
	void exitInfixexp(HaskellParser.InfixexpContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#exp10p}.
	 * @param ctx the parse tree
	 */
	void enterExp10p(HaskellParser.Exp10pContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#exp10p}.
	 * @param ctx the parse tree
	 */
	void exitExp10p(HaskellParser.Exp10pContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#exp10}.
	 * @param ctx the parse tree
	 */
	void enterExp10(HaskellParser.Exp10Context ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#exp10}.
	 * @param ctx the parse tree
	 */
	void exitExp10(HaskellParser.Exp10Context ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#fexp}.
	 * @param ctx the parse tree
	 */
	void enterFexp(HaskellParser.FexpContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#fexp}.
	 * @param ctx the parse tree
	 */
	void exitFexp(HaskellParser.FexpContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#aexp}.
	 * @param ctx the parse tree
	 */
	void enterAexp(HaskellParser.AexpContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#aexp}.
	 * @param ctx the parse tree
	 */
	void exitAexp(HaskellParser.AexpContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#aexp1}.
	 * @param ctx the parse tree
	 */
	void enterAexp1(HaskellParser.Aexp1Context ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#aexp1}.
	 * @param ctx the parse tree
	 */
	void exitAexp1(HaskellParser.Aexp1Context ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#aexp2}.
	 * @param ctx the parse tree
	 */
	void enterAexp2(HaskellParser.Aexp2Context ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#aexp2}.
	 * @param ctx the parse tree
	 */
	void exitAexp2(HaskellParser.Aexp2Context ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#splice_exp}.
	 * @param ctx the parse tree
	 */
	void enterSplice_exp(HaskellParser.Splice_expContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#splice_exp}.
	 * @param ctx the parse tree
	 */
	void exitSplice_exp(HaskellParser.Splice_expContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#splice_untyped}.
	 * @param ctx the parse tree
	 */
	void enterSplice_untyped(HaskellParser.Splice_untypedContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#splice_untyped}.
	 * @param ctx the parse tree
	 */
	void exitSplice_untyped(HaskellParser.Splice_untypedContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#splice_typed}.
	 * @param ctx the parse tree
	 */
	void enterSplice_typed(HaskellParser.Splice_typedContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#splice_typed}.
	 * @param ctx the parse tree
	 */
	void exitSplice_typed(HaskellParser.Splice_typedContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#cmdargs}.
	 * @param ctx the parse tree
	 */
	void enterCmdargs(HaskellParser.CmdargsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#cmdargs}.
	 * @param ctx the parse tree
	 */
	void exitCmdargs(HaskellParser.CmdargsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#acmd}.
	 * @param ctx the parse tree
	 */
	void enterAcmd(HaskellParser.AcmdContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#acmd}.
	 * @param ctx the parse tree
	 */
	void exitAcmd(HaskellParser.AcmdContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#cvtopbody}.
	 * @param ctx the parse tree
	 */
	void enterCvtopbody(HaskellParser.CvtopbodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#cvtopbody}.
	 * @param ctx the parse tree
	 */
	void exitCvtopbody(HaskellParser.CvtopbodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#cvtopdecls0}.
	 * @param ctx the parse tree
	 */
	void enterCvtopdecls0(HaskellParser.Cvtopdecls0Context ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#cvtopdecls0}.
	 * @param ctx the parse tree
	 */
	void exitCvtopdecls0(HaskellParser.Cvtopdecls0Context ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#texp}.
	 * @param ctx the parse tree
	 */
	void enterTexp(HaskellParser.TexpContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#texp}.
	 * @param ctx the parse tree
	 */
	void exitTexp(HaskellParser.TexpContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#tup_exprs}.
	 * @param ctx the parse tree
	 */
	void enterTup_exprs(HaskellParser.Tup_exprsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#tup_exprs}.
	 * @param ctx the parse tree
	 */
	void exitTup_exprs(HaskellParser.Tup_exprsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#commas_tup_tail}.
	 * @param ctx the parse tree
	 */
	void enterCommas_tup_tail(HaskellParser.Commas_tup_tailContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#commas_tup_tail}.
	 * @param ctx the parse tree
	 */
	void exitCommas_tup_tail(HaskellParser.Commas_tup_tailContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#tup_tail}.
	 * @param ctx the parse tree
	 */
	void enterTup_tail(HaskellParser.Tup_tailContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#tup_tail}.
	 * @param ctx the parse tree
	 */
	void exitTup_tail(HaskellParser.Tup_tailContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#lst}.
	 * @param ctx the parse tree
	 */
	void enterLst(HaskellParser.LstContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#lst}.
	 * @param ctx the parse tree
	 */
	void exitLst(HaskellParser.LstContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#lexps}.
	 * @param ctx the parse tree
	 */
	void enterLexps(HaskellParser.LexpsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#lexps}.
	 * @param ctx the parse tree
	 */
	void exitLexps(HaskellParser.LexpsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#flattenedpquals}.
	 * @param ctx the parse tree
	 */
	void enterFlattenedpquals(HaskellParser.FlattenedpqualsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#flattenedpquals}.
	 * @param ctx the parse tree
	 */
	void exitFlattenedpquals(HaskellParser.FlattenedpqualsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#pquals}.
	 * @param ctx the parse tree
	 */
	void enterPquals(HaskellParser.PqualsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#pquals}.
	 * @param ctx the parse tree
	 */
	void exitPquals(HaskellParser.PqualsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#squals}.
	 * @param ctx the parse tree
	 */
	void enterSquals(HaskellParser.SqualsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#squals}.
	 * @param ctx the parse tree
	 */
	void exitSquals(HaskellParser.SqualsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#transformqual}.
	 * @param ctx the parse tree
	 */
	void enterTransformqual(HaskellParser.TransformqualContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#transformqual}.
	 * @param ctx the parse tree
	 */
	void exitTransformqual(HaskellParser.TransformqualContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#guards}.
	 * @param ctx the parse tree
	 */
	void enterGuards(HaskellParser.GuardsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#guards}.
	 * @param ctx the parse tree
	 */
	void exitGuards(HaskellParser.GuardsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#guard}.
	 * @param ctx the parse tree
	 */
	void enterGuard(HaskellParser.GuardContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#guard}.
	 * @param ctx the parse tree
	 */
	void exitGuard(HaskellParser.GuardContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#alts}.
	 * @param ctx the parse tree
	 */
	void enterAlts(HaskellParser.AltsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#alts}.
	 * @param ctx the parse tree
	 */
	void exitAlts(HaskellParser.AltsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#alt}.
	 * @param ctx the parse tree
	 */
	void enterAlt(HaskellParser.AltContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#alt}.
	 * @param ctx the parse tree
	 */
	void exitAlt(HaskellParser.AltContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#alt_rhs}.
	 * @param ctx the parse tree
	 */
	void enterAlt_rhs(HaskellParser.Alt_rhsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#alt_rhs}.
	 * @param ctx the parse tree
	 */
	void exitAlt_rhs(HaskellParser.Alt_rhsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#ralt}.
	 * @param ctx the parse tree
	 */
	void enterRalt(HaskellParser.RaltContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#ralt}.
	 * @param ctx the parse tree
	 */
	void exitRalt(HaskellParser.RaltContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#gdpats}.
	 * @param ctx the parse tree
	 */
	void enterGdpats(HaskellParser.GdpatsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#gdpats}.
	 * @param ctx the parse tree
	 */
	void exitGdpats(HaskellParser.GdpatsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#ifgdpats}.
	 * @param ctx the parse tree
	 */
	void enterIfgdpats(HaskellParser.IfgdpatsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#ifgdpats}.
	 * @param ctx the parse tree
	 */
	void exitIfgdpats(HaskellParser.IfgdpatsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#gdpat}.
	 * @param ctx the parse tree
	 */
	void enterGdpat(HaskellParser.GdpatContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#gdpat}.
	 * @param ctx the parse tree
	 */
	void exitGdpat(HaskellParser.GdpatContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#pat}.
	 * @param ctx the parse tree
	 */
	void enterPat(HaskellParser.PatContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#pat}.
	 * @param ctx the parse tree
	 */
	void exitPat(HaskellParser.PatContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#bindpat}.
	 * @param ctx the parse tree
	 */
	void enterBindpat(HaskellParser.BindpatContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#bindpat}.
	 * @param ctx the parse tree
	 */
	void exitBindpat(HaskellParser.BindpatContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#apat}.
	 * @param ctx the parse tree
	 */
	void enterApat(HaskellParser.ApatContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#apat}.
	 * @param ctx the parse tree
	 */
	void exitApat(HaskellParser.ApatContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#apats}.
	 * @param ctx the parse tree
	 */
	void enterApats(HaskellParser.ApatsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#apats}.
	 * @param ctx the parse tree
	 */
	void exitApats(HaskellParser.ApatsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#fpat}.
	 * @param ctx the parse tree
	 */
	void enterFpat(HaskellParser.FpatContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#fpat}.
	 * @param ctx the parse tree
	 */
	void exitFpat(HaskellParser.FpatContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#stmtlist}.
	 * @param ctx the parse tree
	 */
	void enterStmtlist(HaskellParser.StmtlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#stmtlist}.
	 * @param ctx the parse tree
	 */
	void exitStmtlist(HaskellParser.StmtlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#stmts}.
	 * @param ctx the parse tree
	 */
	void enterStmts(HaskellParser.StmtsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#stmts}.
	 * @param ctx the parse tree
	 */
	void exitStmts(HaskellParser.StmtsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterStmt(HaskellParser.StmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitStmt(HaskellParser.StmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#qual}.
	 * @param ctx the parse tree
	 */
	void enterQual(HaskellParser.QualContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#qual}.
	 * @param ctx the parse tree
	 */
	void exitQual(HaskellParser.QualContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#fbinds}.
	 * @param ctx the parse tree
	 */
	void enterFbinds(HaskellParser.FbindsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#fbinds}.
	 * @param ctx the parse tree
	 */
	void exitFbinds(HaskellParser.FbindsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#fbind}.
	 * @param ctx the parse tree
	 */
	void enterFbind(HaskellParser.FbindContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#fbind}.
	 * @param ctx the parse tree
	 */
	void exitFbind(HaskellParser.FbindContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#dbinds}.
	 * @param ctx the parse tree
	 */
	void enterDbinds(HaskellParser.DbindsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#dbinds}.
	 * @param ctx the parse tree
	 */
	void exitDbinds(HaskellParser.DbindsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#dbind}.
	 * @param ctx the parse tree
	 */
	void enterDbind(HaskellParser.DbindContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#dbind}.
	 * @param ctx the parse tree
	 */
	void exitDbind(HaskellParser.DbindContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#name_boolformula_opt}.
	 * @param ctx the parse tree
	 */
	void enterName_boolformula_opt(HaskellParser.Name_boolformula_optContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#name_boolformula_opt}.
	 * @param ctx the parse tree
	 */
	void exitName_boolformula_opt(HaskellParser.Name_boolformula_optContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#name_boolformula_and}.
	 * @param ctx the parse tree
	 */
	void enterName_boolformula_and(HaskellParser.Name_boolformula_andContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#name_boolformula_and}.
	 * @param ctx the parse tree
	 */
	void exitName_boolformula_and(HaskellParser.Name_boolformula_andContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#name_boolformula_and_list}.
	 * @param ctx the parse tree
	 */
	void enterName_boolformula_and_list(HaskellParser.Name_boolformula_and_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#name_boolformula_and_list}.
	 * @param ctx the parse tree
	 */
	void exitName_boolformula_and_list(HaskellParser.Name_boolformula_and_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#name_boolformula_atom}.
	 * @param ctx the parse tree
	 */
	void enterName_boolformula_atom(HaskellParser.Name_boolformula_atomContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#name_boolformula_atom}.
	 * @param ctx the parse tree
	 */
	void exitName_boolformula_atom(HaskellParser.Name_boolformula_atomContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#namelist}.
	 * @param ctx the parse tree
	 */
	void enterNamelist(HaskellParser.NamelistContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#namelist}.
	 * @param ctx the parse tree
	 */
	void exitNamelist(HaskellParser.NamelistContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#name_var}.
	 * @param ctx the parse tree
	 */
	void enterName_var(HaskellParser.Name_varContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#name_var}.
	 * @param ctx the parse tree
	 */
	void exitName_var(HaskellParser.Name_varContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#qcon_nowiredlist}.
	 * @param ctx the parse tree
	 */
	void enterQcon_nowiredlist(HaskellParser.Qcon_nowiredlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#qcon_nowiredlist}.
	 * @param ctx the parse tree
	 */
	void exitQcon_nowiredlist(HaskellParser.Qcon_nowiredlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#qcon}.
	 * @param ctx the parse tree
	 */
	void enterQcon(HaskellParser.QconContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#qcon}.
	 * @param ctx the parse tree
	 */
	void exitQcon(HaskellParser.QconContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#gen_qcon}.
	 * @param ctx the parse tree
	 */
	void enterGen_qcon(HaskellParser.Gen_qconContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#gen_qcon}.
	 * @param ctx the parse tree
	 */
	void exitGen_qcon(HaskellParser.Gen_qconContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#con}.
	 * @param ctx the parse tree
	 */
	void enterCon(HaskellParser.ConContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#con}.
	 * @param ctx the parse tree
	 */
	void exitCon(HaskellParser.ConContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#con_list}.
	 * @param ctx the parse tree
	 */
	void enterCon_list(HaskellParser.Con_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#con_list}.
	 * @param ctx the parse tree
	 */
	void exitCon_list(HaskellParser.Con_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#sysdcon_nolist}.
	 * @param ctx the parse tree
	 */
	void enterSysdcon_nolist(HaskellParser.Sysdcon_nolistContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#sysdcon_nolist}.
	 * @param ctx the parse tree
	 */
	void exitSysdcon_nolist(HaskellParser.Sysdcon_nolistContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#sysdcon}.
	 * @param ctx the parse tree
	 */
	void enterSysdcon(HaskellParser.SysdconContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#sysdcon}.
	 * @param ctx the parse tree
	 */
	void exitSysdcon(HaskellParser.SysdconContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#conop}.
	 * @param ctx the parse tree
	 */
	void enterConop(HaskellParser.ConopContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#conop}.
	 * @param ctx the parse tree
	 */
	void exitConop(HaskellParser.ConopContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#qconop}.
	 * @param ctx the parse tree
	 */
	void enterQconop(HaskellParser.QconopContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#qconop}.
	 * @param ctx the parse tree
	 */
	void exitQconop(HaskellParser.QconopContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#gconsym}.
	 * @param ctx the parse tree
	 */
	void enterGconsym(HaskellParser.GconsymContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#gconsym}.
	 * @param ctx the parse tree
	 */
	void exitGconsym(HaskellParser.GconsymContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#gtycon}.
	 * @param ctx the parse tree
	 */
	void enterGtycon(HaskellParser.GtyconContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#gtycon}.
	 * @param ctx the parse tree
	 */
	void exitGtycon(HaskellParser.GtyconContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#ntgtycon}.
	 * @param ctx the parse tree
	 */
	void enterNtgtycon(HaskellParser.NtgtyconContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#ntgtycon}.
	 * @param ctx the parse tree
	 */
	void exitNtgtycon(HaskellParser.NtgtyconContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#oqtycon}.
	 * @param ctx the parse tree
	 */
	void enterOqtycon(HaskellParser.OqtyconContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#oqtycon}.
	 * @param ctx the parse tree
	 */
	void exitOqtycon(HaskellParser.OqtyconContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#qtyconop}.
	 * @param ctx the parse tree
	 */
	void enterQtyconop(HaskellParser.QtyconopContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#qtyconop}.
	 * @param ctx the parse tree
	 */
	void exitQtyconop(HaskellParser.QtyconopContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#qtycon}.
	 * @param ctx the parse tree
	 */
	void enterQtycon(HaskellParser.QtyconContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#qtycon}.
	 * @param ctx the parse tree
	 */
	void exitQtycon(HaskellParser.QtyconContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#tycon}.
	 * @param ctx the parse tree
	 */
	void enterTycon(HaskellParser.TyconContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#tycon}.
	 * @param ctx the parse tree
	 */
	void exitTycon(HaskellParser.TyconContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#qtyconsym}.
	 * @param ctx the parse tree
	 */
	void enterQtyconsym(HaskellParser.QtyconsymContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#qtyconsym}.
	 * @param ctx the parse tree
	 */
	void exitQtyconsym(HaskellParser.QtyconsymContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#tyconsym}.
	 * @param ctx the parse tree
	 */
	void enterTyconsym(HaskellParser.TyconsymContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#tyconsym}.
	 * @param ctx the parse tree
	 */
	void exitTyconsym(HaskellParser.TyconsymContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#op}.
	 * @param ctx the parse tree
	 */
	void enterOp(HaskellParser.OpContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#op}.
	 * @param ctx the parse tree
	 */
	void exitOp(HaskellParser.OpContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#varop}.
	 * @param ctx the parse tree
	 */
	void enterVarop(HaskellParser.VaropContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#varop}.
	 * @param ctx the parse tree
	 */
	void exitVarop(HaskellParser.VaropContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#qop}.
	 * @param ctx the parse tree
	 */
	void enterQop(HaskellParser.QopContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#qop}.
	 * @param ctx the parse tree
	 */
	void exitQop(HaskellParser.QopContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#qopm}.
	 * @param ctx the parse tree
	 */
	void enterQopm(HaskellParser.QopmContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#qopm}.
	 * @param ctx the parse tree
	 */
	void exitQopm(HaskellParser.QopmContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#hole_op}.
	 * @param ctx the parse tree
	 */
	void enterHole_op(HaskellParser.Hole_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#hole_op}.
	 * @param ctx the parse tree
	 */
	void exitHole_op(HaskellParser.Hole_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#qvarop}.
	 * @param ctx the parse tree
	 */
	void enterQvarop(HaskellParser.QvaropContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#qvarop}.
	 * @param ctx the parse tree
	 */
	void exitQvarop(HaskellParser.QvaropContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#qvaropm}.
	 * @param ctx the parse tree
	 */
	void enterQvaropm(HaskellParser.QvaropmContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#qvaropm}.
	 * @param ctx the parse tree
	 */
	void exitQvaropm(HaskellParser.QvaropmContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#tyvar}.
	 * @param ctx the parse tree
	 */
	void enterTyvar(HaskellParser.TyvarContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#tyvar}.
	 * @param ctx the parse tree
	 */
	void exitTyvar(HaskellParser.TyvarContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#tyvarop}.
	 * @param ctx the parse tree
	 */
	void enterTyvarop(HaskellParser.TyvaropContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#tyvarop}.
	 * @param ctx the parse tree
	 */
	void exitTyvarop(HaskellParser.TyvaropContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#tyvarid}.
	 * @param ctx the parse tree
	 */
	void enterTyvarid(HaskellParser.TyvaridContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#tyvarid}.
	 * @param ctx the parse tree
	 */
	void exitTyvarid(HaskellParser.TyvaridContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#tycls}.
	 * @param ctx the parse tree
	 */
	void enterTycls(HaskellParser.TyclsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#tycls}.
	 * @param ctx the parse tree
	 */
	void exitTycls(HaskellParser.TyclsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#qtycls}.
	 * @param ctx the parse tree
	 */
	void enterQtycls(HaskellParser.QtyclsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#qtycls}.
	 * @param ctx the parse tree
	 */
	void exitQtycls(HaskellParser.QtyclsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#var}.
	 * @param ctx the parse tree
	 */
	void enterVar(HaskellParser.VarContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#var}.
	 * @param ctx the parse tree
	 */
	void exitVar(HaskellParser.VarContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#qvar}.
	 * @param ctx the parse tree
	 */
	void enterQvar(HaskellParser.QvarContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#qvar}.
	 * @param ctx the parse tree
	 */
	void exitQvar(HaskellParser.QvarContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#qvarid}.
	 * @param ctx the parse tree
	 */
	void enterQvarid(HaskellParser.QvaridContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#qvarid}.
	 * @param ctx the parse tree
	 */
	void exitQvarid(HaskellParser.QvaridContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#varid}.
	 * @param ctx the parse tree
	 */
	void enterVarid(HaskellParser.VaridContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#varid}.
	 * @param ctx the parse tree
	 */
	void exitVarid(HaskellParser.VaridContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#qvarsym}.
	 * @param ctx the parse tree
	 */
	void enterQvarsym(HaskellParser.QvarsymContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#qvarsym}.
	 * @param ctx the parse tree
	 */
	void exitQvarsym(HaskellParser.QvarsymContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#qvarsym_no_minus}.
	 * @param ctx the parse tree
	 */
	void enterQvarsym_no_minus(HaskellParser.Qvarsym_no_minusContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#qvarsym_no_minus}.
	 * @param ctx the parse tree
	 */
	void exitQvarsym_no_minus(HaskellParser.Qvarsym_no_minusContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#varsym}.
	 * @param ctx the parse tree
	 */
	void enterVarsym(HaskellParser.VarsymContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#varsym}.
	 * @param ctx the parse tree
	 */
	void exitVarsym(HaskellParser.VarsymContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#varsym_no_minus}.
	 * @param ctx the parse tree
	 */
	void enterVarsym_no_minus(HaskellParser.Varsym_no_minusContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#varsym_no_minus}.
	 * @param ctx the parse tree
	 */
	void exitVarsym_no_minus(HaskellParser.Varsym_no_minusContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#special_id}.
	 * @param ctx the parse tree
	 */
	void enterSpecial_id(HaskellParser.Special_idContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#special_id}.
	 * @param ctx the parse tree
	 */
	void exitSpecial_id(HaskellParser.Special_idContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#qconid}.
	 * @param ctx the parse tree
	 */
	void enterQconid(HaskellParser.QconidContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#qconid}.
	 * @param ctx the parse tree
	 */
	void exitQconid(HaskellParser.QconidContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#conid}.
	 * @param ctx the parse tree
	 */
	void enterConid(HaskellParser.ConidContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#conid}.
	 * @param ctx the parse tree
	 */
	void exitConid(HaskellParser.ConidContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#qconsym}.
	 * @param ctx the parse tree
	 */
	void enterQconsym(HaskellParser.QconsymContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#qconsym}.
	 * @param ctx the parse tree
	 */
	void exitQconsym(HaskellParser.QconsymContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#consym}.
	 * @param ctx the parse tree
	 */
	void enterConsym(HaskellParser.ConsymContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#consym}.
	 * @param ctx the parse tree
	 */
	void exitConsym(HaskellParser.ConsymContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(HaskellParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(HaskellParser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#opn}.
	 * @param ctx the parse tree
	 */
	void enterOpn(HaskellParser.OpnContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#opn}.
	 * @param ctx the parse tree
	 */
	void exitOpn(HaskellParser.OpnContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#close}.
	 * @param ctx the parse tree
	 */
	void enterClose(HaskellParser.CloseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#close}.
	 * @param ctx the parse tree
	 */
	void exitClose(HaskellParser.CloseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#semi}.
	 * @param ctx the parse tree
	 */
	void enterSemi(HaskellParser.SemiContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#semi}.
	 * @param ctx the parse tree
	 */
	void exitSemi(HaskellParser.SemiContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#modid}.
	 * @param ctx the parse tree
	 */
	void enterModid(HaskellParser.ModidContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#modid}.
	 * @param ctx the parse tree
	 */
	void exitModid(HaskellParser.ModidContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#commas}.
	 * @param ctx the parse tree
	 */
	void enterCommas(HaskellParser.CommasContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#commas}.
	 * @param ctx the parse tree
	 */
	void exitCommas(HaskellParser.CommasContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#bars}.
	 * @param ctx the parse tree
	 */
	void enterBars(HaskellParser.BarsContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#bars}.
	 * @param ctx the parse tree
	 */
	void exitBars(HaskellParser.BarsContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#special}.
	 * @param ctx the parse tree
	 */
	void enterSpecial(HaskellParser.SpecialContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#special}.
	 * @param ctx the parse tree
	 */
	void exitSpecial(HaskellParser.SpecialContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#symbol}.
	 * @param ctx the parse tree
	 */
	void enterSymbol(HaskellParser.SymbolContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#symbol}.
	 * @param ctx the parse tree
	 */
	void exitSymbol(HaskellParser.SymbolContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#ascSymbol}.
	 * @param ctx the parse tree
	 */
	void enterAscSymbol(HaskellParser.AscSymbolContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#ascSymbol}.
	 * @param ctx the parse tree
	 */
	void exitAscSymbol(HaskellParser.AscSymbolContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#integer}.
	 * @param ctx the parse tree
	 */
	void enterInteger(HaskellParser.IntegerContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#integer}.
	 * @param ctx the parse tree
	 */
	void exitInteger(HaskellParser.IntegerContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#pfloat}.
	 * @param ctx the parse tree
	 */
	void enterPfloat(HaskellParser.PfloatContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#pfloat}.
	 * @param ctx the parse tree
	 */
	void exitPfloat(HaskellParser.PfloatContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#pchar}.
	 * @param ctx the parse tree
	 */
	void enterPchar(HaskellParser.PcharContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#pchar}.
	 * @param ctx the parse tree
	 */
	void exitPchar(HaskellParser.PcharContext ctx);
	/**
	 * Enter a parse tree produced by {@link HaskellParser#pstring}.
	 * @param ctx the parse tree
	 */
	void enterPstring(HaskellParser.PstringContext ctx);
	/**
	 * Exit a parse tree produced by {@link HaskellParser#pstring}.
	 * @param ctx the parse tree
	 */
	void exitPstring(HaskellParser.PstringContext ctx);
}